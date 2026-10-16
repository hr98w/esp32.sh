"""Discover candidates from existing directories, never blind repository search."""
import argparse
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from public_fetch import fetch_public, utc_now, Deferred, ROOT, _write, _read

class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.current=None; self.jsonld=[]; self.script=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='a': self.current=[a.get('href',''),[]]
        if tag=='script' and a.get('type')=='application/ld+json': self.script=[]
    def handle_data(self,data):
        if self.current is not None: self.current[1].append(data)
        if self.script is not None: self.script.append(data)
    def handle_endtag(self,tag):
        if tag=='a' and self.current is not None:
            self.links.append((self.current[0],' '.join(self.current[1]).strip()));self.current=None
        if tag=='script' and self.script is not None:
            try:self.jsonld.append(json.loads(''.join(self.script)))
            except json.JSONDecodeError:pass
            self.script=None

SOURCES=[
 ('espboards','devices','https://www.espboards.dev/esp32/'),
 ('espboards-sitemap','devices','https://www.espboards.dev/sitemap.xml'),
 ('m5ware','projects','https://m5ware.com/'),
 ('awesome-esp32','projects','https://api.github.com/repos/s0lness/awesome-esp32/readme'),
]

def repo_from_url(value):
    value=html.unescape(value).strip().rstrip(').,')
    match=re.match(r'https://github\.com/([\w.-]+)/([\w.-]+)(?:[/#?]|$)',value)
    if not match:return None
    owner,repo=match.groups()
    if owner.lower() in {'topics','orgs','settings','features','sponsors','collections','marketplace','login','signup','search','explore'}:return None
    return owner+'/'+repo.removesuffix('.git')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--online',action='store_true');args=parser.parse_args()
    ledger_path=ROOT/'data/collection/project-candidates.json'
    projects=_read(ledger_path,{})
    source_log=_read(ROOT/'data/collection/sources.json',{})
    device_urls=set(_read(ROOT/'data/collection/device-source-urls.json',[]))
    for key,kind,url in SOURCES:
        try:
            result=fetch_public(url,accept='application/vnd.github.raw+json' if key=='awesome-esp32' else 'text/html',offline=not args.online)
            body=result['body'].decode(errors='replace')
            links=Links();links.feed(body)
            source_log[key]={'url':url,'kind':kind,'checkedAt':result['checkedAt'],'status':'discovered','next':'upstream verification'}
            if kind=='devices':
                for href,_ in links.links:
                    full=urljoin(url,href)
                    if re.match(r'https://www\.espboards\.dev/esp32/[^/]+/?$',full) and not any(x in full for x in ['/popular','/best']):device_urls.add(full)
                for loc in re.findall(r'<loc>(.*?)</loc>',body):
                    if '/esp32/' in loc:device_urls.add(html.unescape(loc))
            else:
                matches=[(href,title) for href,title in links.links if repo_from_url(href)]
                matches += [(v,'') for v in re.findall(r'https://github\.com/[\w.-]+/[\w.-]+(?:[^\s<>"\)]*)?',body)]
                matches += [(match[2],match[1]) for match in re.finditer(r'\[([^]]+)\]\((https://github\.com/[^)]+)\)',body)]
                for href,title in matches:
                    repo=repo_from_url(href)
                    if not repo:continue
                    identity=repo.lower()
                    record=projects.setdefault(identity,{'repository':repo,'status':'discovered','discoveredAt':utc_now(),'sources':[],'reason':None})
                    source_url='https://github.com/s0lness/awesome-esp32' if key=='awesome-esp32' else url
                    if source_url not in record['sources']:record['sources'].append(source_url)
                    if title and not record.get('directoryTitle'):record['directoryTitle']=title
                    if key=='awesome-esp32':
                        line=next((line for line in body.splitlines() if href in line),'')
                        if line:record['directoryDescription']=line
            print(f'{key}: {len(body)} bytes, {len(links.links)} links')
        except (RuntimeError,Deferred) as error:
            source_log[key]={'url':url,'kind':kind,'status':'deferred','reason':str(error),'attemptedAt':utc_now()}
            print(f'{key}: {error}')
    _write(ledger_path,projects);_write(ROOT/'data/collection/sources.json',source_log);_write(ROOT/'data/collection/device-source-urls.json',sorted(device_urls))
    print(f'Candidates: {len(projects)} repository links; {len(device_urls)} ESPboards URLs (classification pending).')

if __name__=='__main__':main()
