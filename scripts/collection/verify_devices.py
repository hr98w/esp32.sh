import argparse,re
from urllib.parse import urlparse
from public_fetch import fetch_public,_read,_write,ROOT,Deferred
from discover_devices import clean

def main():
    p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');p.add_argument('--max',type=int,default=80);p.add_argument('--retry-review',action='store_true');args=p.parse_args()
    path=ROOT/'data/collection/device-candidates.json';records=_read(path,{})
    overrides=_read(ROOT/'data/collection/device-source-overrides.json',{})
    count=0
    for key,record in records.items():
        d=record.get('details')
        if not d:continue
        override=overrides.get(record['id'])
        if override and override['url']!=d.get('officialUrl'):
            d.update(originalSourceUrl=d.get('officialUrl'),officialUrl=override['url'],primaryStatus='pending',sourceOverrideReason=override['reason'])
            for field in ['primaryReason','primaryTitle','primaryExcerpt','primaryTextCharacters','primaryCheckedAt']:d.pop(field,None)
        if not d.get('officialUrl') or d.get('primaryStatus')=='checked' or (d.get('primaryStatus')=='needs-review' and not args.retry_review):continue
        url=d['officialUrl'];host=urlparse(url).hostname or ''
        if host in {'github.com','raw.githubusercontent.com','api.github.com'}:continue
        if host in {'amzn.to','amazon.com','aliexpress.com','banggood.com'} or host.endswith(('.etsy.com','.amazon.com','.aliexpress.com')):
            d.update(primaryStatus='needs-review',primaryReason='Only a reseller URL found');continue
        if count>=args.max:break
        try:
            result=fetch_public(url,offline=not args.online)
            if result['body'].startswith(b'%PDF'):
                d.update(primaryStatus='needs-review',primaryReason='PDF source requires document review; not parsed as HTML')
                for field in ['primaryTitle','primaryExcerpt','primaryTextCharacters']:d.pop(field,None)
                _write(path,records);count+=1;continue
            body=result['body'].decode(errors='replace')
            title=re.search(r'<title[^>]*>(.*?)</title>',body,re.S)
            content=clean(re.sub(r'<(?:script|style)[^>]*>[\s\S]*?</(?:script|style)>',' ',body))
            d.update(primaryStatus='checked',primaryCheckedAt=result['checkedAt'],primaryTitle=clean(title[1]) if title else '',primaryExcerpt=content[:1200],primaryTextCharacters=len(content))
            # Retain source text only in local cache; facts require editorial source review before publication.
            print('Primary',record['id'],d['primaryTitle'][:100],flush=True)
        except (RuntimeError,Deferred) as error:
            d.update(primaryStatus='needs-review',primaryReason=str(error));print(record['id'],error,flush=True)
        count+=1;_write(path,records)
    _write(path,records)

if __name__=='__main__':main()
