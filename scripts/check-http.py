"""Read-only local production smoke checks. Start pnpm preview --port 4317 first."""
import json,sys
from html import unescape
from urllib.request import build_opener,ProxyHandler,HTTPRedirectHandler
from urllib.error import HTTPError
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import quote, urlsplit, parse_qs
base=sys.argv[1] if len(sys.argv)>1 else 'http://localhost:4317'
class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):return None
normal=build_opener(ProxyHandler({}));raw=build_opener(ProxyHandler({}),NoRedirect)
def request(path,follow=True):
    try:r=(normal if follow else raw).open(base+path,timeout=20)
    except HTTPError as error:r=error
    with r:return r.status,r.read().decode(),r.headers
class Page(HTMLParser):
    def __init__(self,html):super().__init__();self.cards=0;self.project_links=[];self.headings=[];self.images=[];self.feed(html)
    def handle_starttag(self,tag,attrs):
        if ('class','project-card') in attrs:self.cards+=1
        values=dict(attrs)
        if tag=='a' and 'cover' in values.get('class','').split():self.project_links.append(values['href'])
        if tag=='h2' and values.get('id'):self.headings.append(values['id'])
        if tag=='img':self.images.append(values['src'])
catalog=json.loads(Path('src/generated/catalog.json').read_text())
status,html,_=request('/',False)
assert status==200 and '<html lang="en"' in html
assert 'href="/devices"' in html and 'q=&amp;' not in html
for locale,prefix,html_lang in [('en','','en'),('zh','/zh','zh-CN'),('ja','/ja','ja')]:
    for path in [prefix or '/',prefix+'/devices',prefix+'/devices/m5stack-cardputer']:
        status,html,_=request(path);assert status==200 and f'<html lang="{html_lang}"' in html,(path,status)
for path,expected in [('/',len(catalog['projects'])),('/?device=waveshare-esp32-s3-touch-amoled-1-8',sum(any(d['deviceId']=='waveshare-esp32-s3-touch-amoled-1-8' for d in p['devices']) for p in catalog['projects'])),('/?q=zzzznonexistent',0),('/devices?maker=m5stack',sum(d['manufacturer']['id']=='m5stack' for d in catalog['devices'])),('/devices?feature=keyboard',sum('keyboard' in d['features'] for d in catalog['devices'])),('/devices?feature=display',sum('display' in d['features'] or 'epaper' in d['features'] for d in catalog['devices'])),('/devices?q=M5CardputerADV',1),('/devices?q=Seeed%20XIAO',sum(d['manufacturer']['id']=='seeed-studio' and d['name'].lower().startswith('xiao') for d in catalog['devices'])),('/devices?q=zzzznonexistent',0)]:
    status,html,_=request(path);assert status==200 and Page(html).cards==min(24,expected),(path,status,Page(html).cards,min(24,expected))
# Traverse both directories in every locale: no missing or duplicated cards.
for prefix in ['', '/zh', '/ja']:
    for suffix, entries, expected in [('', catalog['projects'], {p['repository'] for p in catalog['projects']}), ('/devices', catalog['devices'], {prefix+'/devices/'+d['id'] for d in catalog['devices']})]:
        seen=[]
        root=prefix+suffix or '/'
        for page_number in range(1,(len(entries)+23)//24+1):
            path=root+('?page='+str(page_number) if page_number>1 else '')
            status,html,_=request(path)
            parsed=Page(html)
            assert status==200 and parsed.cards==min(24,len(entries)-(page_number-1)*24),(path,parsed.cards)
            seen.extend(parsed.project_links)
            assert 'aria-current="page"' in html,(path,'missing current page')
            canonical='https://esp32.sh'+root+('?page='+str(page_number) if page_number>1 else '')
            assert 'rel="canonical" href="'+canonical+'"' in html,(path,'canonical page URL')
            if page_number>1:assert '?page=1\"' not in html and '&amp;page=1\"' not in html,(path,'page one must be clean')
        assert set(seen)==expected and len(seen)==len(expected),(root,'missing or duplicate cards')
# Invalid/out-of-range links redirect once, retaining active filters and locale.
for path,target in [('/?page=1','/'),('/?page=oops','/'),('/?page=-2','/'),('/?page=1.5','/'),('/?page=999','/?page='+str((len(catalog['projects'])+23)//24)),('/zh?device=m5stack-stopwatch&page=999','/zh?device=m5stack-stopwatch'),('/ja/devices?q=zzzznonexistent&page=2','/ja/devices?q=zzzznonexistent')]:
    status,_,headers=request(path,False)
    assert status in [301,302,307,308] and headers['Location']==target,(path,status,headers.get('Location'))
    assert request(target)[0]==200,target
# A filtered second page must retain its query in navigation links.
status,html,_=request('/?sort=name&page=2')
assert status==200 and 'sort=name&amp;page=3' in html and 'href="/?sort=name"' in html
maker_counts={d['manufacturer']['id']:sum(x['manufacturer']['id']==d['manufacturer']['id'] for x in catalog['devices']) for d in catalog['devices']}
maker=max(maker_counts,key=maker_counts.get)
if maker_counts[maker]>24:
    status,html,_=request('/devices?maker='+maker+'&page=2')
    assert status==200 and 'href="/devices?maker='+maker+'"' in html and 'aria-current="page"' in html


status,_,headers=request('/en/devices/m5stack-cardputer?q=Bruce',False)
assert status==301 and headers['Location']=='/devices/m5stack-cardputer?q=Bruce'
for path in ['/fr','/devices/not-a-device']:
    assert request(path)[0]==404,path
for locale,prefix,html_lang in [('en','','en'),('zh','/zh','zh-CN'),('ja','/ja','ja')]:
    for device in catalog['devices']:
        path=prefix+'/devices/'+device['id']
        status,html,_=request(path)
        assert status==200 and f'<html lang="{html_lang}"' in html,path
        assert device['name'] in unescape(html) and device['summary'][locale] in unescape(html),path
        parsed=Page(html)
        expected={p['repository']:p for p in catalog['projects'] if any(r['deviceId']==device['id'] for r in p['devices'])}
        assert set(parsed.project_links)==set(expected) and len(parsed.project_links)==len(expected),(path,'related project membership')
        stars=[expected[url].get('metrics',{}).get('stars',-1) for url in parsed.project_links]
        assert stars==sorted(stars,reverse=True),(path,'related project order')
        assert parsed.headings[-1]=='related-projects',(path,'related projects must be the last section')
        for image in [device.get('cover')]+[g['image'] for g in device.get('gallery',[])]:
            if image:assert image.startswith('https://') and image in parsed.images,(path,image)
print(f"Passed local Workers HTTP: 3 languages, root URL, paginated directories in all languages, filters, redirects, 404s, {len(catalog['devices'])*3} localized device pages; direct external device images, translated summaries, related projects last and Star-descending.")
