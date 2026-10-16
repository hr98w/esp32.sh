import argparse,html,json,re
from urllib.parse import urlparse,urljoin,urlsplit,urlunsplit,parse_qsl,urlencode
from public_fetch import fetch_public,_read,_write,ROOT,utc_now,Deferred
from discover import Links

PRIORITY=['m5stack','lilygo','waveshare','seeed-studio','espressif','elecrow','adafruit','unexpected-maker','generic']

def clean(value): return ' '.join(html.unescape(re.sub('<[^>]+>',' ',value)).split())
def extract(body,url):
    title=re.search(r'<h1[^>]*>(.*?)</h1>',body,re.S)
    maker=re.search(r'<p class="byline">.*?<a href="/esp32/manufacturer/([^/]+)/">(.*?)</a>',body,re.S)
    chip=re.search(r'/esp32/microcontroller/([^/]+)/',body)
    description=re.search(r'<p class="sub">(.*?)</p>',body,re.S)
    if not title or not chip:raise ValueError('Missing title/chip; not a confirmed device page')
    links=Links();links.feed(body)
    primary=[(href,label) for href,label in links.links if href.startswith('https://') and any(word in label.lower() for word in ['datasheet','documentation','official','wiki','guide','product page']) and 'espboards.' not in urlparse(href).hostname]
    external=[href for href,label in links.links if href.startswith('https://') and any(word in label for word in ['Store','Buy on'])]
    # Device-level HTML documentation is preferable to a chip/module PDF.
    primary.sort(key=lambda item: (urlparse(item[0]).path.lower().endswith('.pdf'), 'product page' in item[1].lower()))
    chosen=primary[0][0] if primary else next(iter(external),None)
    override=_read(ROOT/'data/collection/device-source-overrides.json',{}).get(urlparse(url).path.strip('/').split('/')[-1])
    if override:chosen=override['url']
    if chosen:
        parsed=urlsplit(chosen)
        query=[(key,value) for key,value in parse_qsl(parsed.query) if not key.lower().startswith('utm_') and key.lower() not in {'ref','tag','aff','aff_id','sensecap_affiliate','referring_service','srsltid'}]
        chosen=urlunsplit((parsed.scheme,parsed.netloc,parsed.path,urlencode(query),parsed.fragment))
    return {'name':clean(title[1]),'manufacturer':{'id':maker[1],'name':clean(maker[2])} if maker else {'id':'unknown','name':'Unknown'},'manufacturerNeedsReview':not bool(maker),'chip':chip[1].upper(),'directoryDescription':clean(description[1]) if description else '', 'officialUrl':chosen,'sourceUrl':url,'sourceCheckedAt':utc_now(),'primaryStatus':'pending'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--online',action='store_true');parser.add_argument('--max',type=int,default=55);parser.add_argument('--manufacturer',action='append');args=parser.parse_args()
    priority=args.manufacturer or PRIORITY
    urls=_read(ROOT/'data/collection/device-source-urls.json',[])
    candidates=_read(ROOT/'data/collection/device-candidates.json',{})
    manufacturers={}
    for url in urls:
        path=urlparse(url).path.strip('/').split('/')
        if len(path)==2 and path[0]=='esp32' and path[1] not in {'best','popular','manufacturers'}:
            candidates.setdefault(url,{'sourceUrl':url,'id':path[1],'status':'discovered','discoveredAt':utc_now()})
        if len(path)==3 and path[1]=='manufacturer':manufacturers[path[2]]=url
    for maker,url in manufacturers.items():
        if maker not in priority:continue
        try:
            result=fetch_public(url,offline=not args.online);links=Links();links.feed(result['body'].decode())
            for href,title in links.links:
                path=urlparse(href).path.strip('/').split('/')
                if len(path)==2 and path[0]=='esp32' and path[1] not in {'best','popular','manufacturers'}:
                    full=urljoin(url,href)
                    entry=candidates.setdefault(full,{'sourceUrl':full,'id':path[1],'status':'discovered','discoveredAt':utc_now()})
                    entry['manufacturerHint']=maker
            print(maker,'indexed',flush=True)
        except (RuntimeError,Deferred) as error:print(error,flush=True)
    _write(ROOT/'data/collection/manufacturer-sources.json',manufacturers)
    _write(ROOT/'data/collection/device-candidates.json',candidates)
    selected=sorted(candidates.items(),key=lambda item:(priority.index(item[1].get('manufacturerHint','unknown')) if item[1].get('manufacturerHint','unknown') in priority else 99,item[0]))
    processed=0
    for url,record in selected:
        if processed>=args.max:break
        if record.get('details'):continue
        if record.get('manufacturerHint','unknown') not in priority:continue
        try:
            result=fetch_public(url,offline=not args.online)
            details=extract(result['body'].decode(),url)
            record.update(details=details,status='needs-review' if details.get('manufacturerNeedsReview') else 'pending',reason='Source directory does not assign a manufacturer; verify upstream brand before publication' if details.get('manufacturerNeedsReview') else 'Primary source and summaries need review')
            print('Device',details['manufacturer']['id'],details['name'],details['chip'],flush=True)
        except (RuntimeError,Deferred,ValueError) as error:
            record.update(status='needs-review',reason=str(error));print(error,flush=True)
        processed+=1;_write(ROOT/'data/collection/device-candidates.json',candidates)
    print('Devices discovered:',len(candidates),'with details:',sum(bool(e.get('details')) for e in candidates.values()),flush=True)

if __name__=='__main__':main()
