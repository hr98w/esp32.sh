import argparse,re
from urllib.parse import urljoin,urlparse
from public_fetch import fetch_public,_read,_write,ROOT,Deferred,utc_now
from discover import Links

def main():
    p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');args=p.parse_args()
    sources=_read(ROOT/'data/collection/manufacturer-sources.json',{})
    progress=_read(ROOT/'data/collection/manufacturer-inventory.json',{})
    for maker,url in sources.items():
        if progress.get(maker,{}).get('status')=='indexed':continue
        try:
            result=fetch_public(url,offline=not args.online);links=Links();links.feed(result['body'].decode())
            records=_read(ROOT/'data/collection/device-candidates.json',{})
            board_urls=[]
            for href,title in links.links:
                parts=urlparse(href).path.strip('/').split('/')
                if len(parts)!=2 or parts[0]!='esp32' or parts[1] in {'best','popular','manufacturers'}:continue
                full=urljoin(url,href);board_urls.append(full)
                record=records.setdefault(full,{'sourceUrl':full,'id':parts[1],'status':'discovered','discoveredAt':utc_now()})
                record['manufacturerHint']=maker
                if not record.get('directoryTitle'):record['directoryTitle']=title
            _write(ROOT/'data/collection/device-candidates.json',records)
            progress[maker]={'sourceUrl':url,'status':'indexed','checkedAt':result['checkedAt'],'discoveredBoards':len(set(board_urls))}
            print(maker,len(set(board_urls)),flush=True)
        except (RuntimeError,Deferred) as error:
            progress[maker]={'sourceUrl':url,'status':'needs-review','reason':str(error)};print(error,flush=True)
        _write(ROOT/'data/collection/manufacturer-inventory.json',progress)

if __name__=='__main__':main()
