"""Collect official device-page evidence for editorial review, never auto-publish.
Uses anonymous cached GETs. Image URLs stay on external manufacturer/CDN hosts.
"""
import argparse, html, json, re
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser
from public_fetch import ROOT, fetch_public, _read, _write, Deferred

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.images=[]; self.links=[]; self.meta={}; self.tables=[]
        self.table=None; self.row=None; self.cell=None; self.link=None; self.skip=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in {'script','style'}: self.skip+=1
        if self.skip:return
        if tag=='meta':self.meta[a.get('property',a.get('name',''))]=a.get('content','')
        if tag=='img':self.images.append({k:a[k] for k in ['src','alt','data-src'] if k in a})
        if tag=='a':self.link={'url':a.get('href',''),'text':''}
        if tag=='table' and self.table is None:self.table=[]
        if tag=='tr' and self.table is not None:self.row=[]
        if tag in {'td','th'} and self.row is not None:self.cell=''
        if tag=='br' and self.cell is not None:self.cell+=' / '
    def handle_endtag(self,tag):
        if tag in {'script','style'}:self.skip=max(0,self.skip-1);return
        if self.skip:return
        if tag=='a' and self.link:
            self.links.append(self.link);self.link=None
        if tag in {'td','th'} and self.cell is not None:
            self.row.append(re.sub(r'\s+',' ',self.cell).strip());self.cell=None
        if tag=='tr' and self.row is not None:
            if self.table is not None:self.table.append(self.row)
            self.row=None
        if tag=='table' and self.table is not None:self.tables.append(self.table);self.table=None
    def handle_data(self,data):
        if self.skip:return
        if self.cell is not None:self.cell+=data
        if self.link is not None:self.link['text']+=data

def extract(body,url):
    p=Page();p.feed(body)
    candidates=[]
    for image in [{'src':p.meta.get('og:image',''),'alt':'Open Graph image'}]+p.images:
        src=image.get('data-src') or image.get('src','')
        if not src:continue
        src=urljoin(url,src)
        if urlparse(src).scheme!='https':continue
        if any(term in src.lower() for term in ['logo','icon','badge','avatar','payment','banner','qr-code','qrcode','paypal']):continue
        if src not in [item['url'] for item in candidates]:candidates.append({'url':src,'alt':image.get('alt','')})
    # The image carousel on M5Stack contains real product photos, before tutorial images.
    if urlparse(url).hostname=='docs.m5stack.com':
        candidates=[{'url':urljoin(url,i['src']),'alt':i.get('alt','')} for i in p.images if i.get('alt')=='Preview' and i.get('src','').startswith('https://')]
    links=[]
    for link in p.links:
        text=re.sub(r'\s+',' ',link['text']).strip();target=urljoin(url,link['url'])
        if not text or not target.startswith('https://'):continue
        if any(term in text.lower() for term in ['arduino','uiflow','quick start','getting started','schematic','datasheet','factory firmware','factory demo','user demo','userdemo','user guide','pinout','download mode']):
            if not any(x['url']==target for x in links):links.append({'label':text[:120],'url':target})
    # Some manufacturer pages omit optional </td> and </tr> tags.
    tables=[]
    for table in re.findall(r'<table\b[^>]*>([\s\S]*?)</table>',body,re.I):
        rows=[]
        for row in re.split(r'<tr\b[^>]*>',table,flags=re.I)[1:]:
            cells=[]
            for match in re.finditer(r'<t[dh]\b[^>]*>([\s\S]*?)(?=</?t[dh]\b|</?tr\b|</?thead\b|</?tbody\b|$)',row,re.I):
                value=re.sub(r'<br\s*/?>',' / ',match[1],flags=re.I)
                value=html.unescape(re.sub(r'<[^>]+>',' ',value))
                cells.append(re.sub(r'\s+',' ',value).strip())
            if cells:rows.append(cells)
        if rows:tables.append(rows)
    return {'images':candidates,'tables':tables,'resources':links,'title':p.meta.get('og:title','')}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--online',action='store_true');parser.add_argument('--maker');parser.add_argument('--max',type=int,default=200);args=parser.parse_args()
    devices=json.loads((ROOT/'src/generated/catalog.json').read_text())['devices']
    devices.sort(key=lambda d:(d['type']!='integrated-device',d['manufacturer']['id'],d['id']))
    path=ROOT/'data/collection/device-enrichment-evidence.json';evidence=_read(path,{})
    processed=0
    for d in devices:
        if args.maker and d['manufacturer']['id']!=args.maker:continue
        if processed>=args.max:break
        if evidence.get(d['id'],{}).get('status')=='collected':continue
        url=d['officialUrl']
        try:
            r=fetch_public(url,ttl=7*86400,offline=not args.online)
            body=r['body'].decode(errors='replace')
            if '<html' not in body.lower():raise RuntimeError('Expected an HTML device page')
            result=extract(body,url)
            evidence[d['id']]={'status':'collected','sourceUrl':url,'checkedAt':r['checkedAt'],**result}
            print(d['id'],len(result['images']),'images',len(result['tables']),'tables',flush=True)
        except (RuntimeError,Deferred) as error:
            evidence[d['id']]={'status':'needs-review','sourceUrl':url,'reason':str(error)}
            print(d['id'],str(error),flush=True)
        _write(path,evidence);processed+=1
if __name__=='__main__':main()
