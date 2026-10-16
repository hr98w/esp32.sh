import argparse,re
from urllib.parse import urljoin
from public_fetch import fetch_public,_write,_read,ROOT,utc_now,Deferred
from discover import Links,repo_from_url

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--online',action='store_true');parser.add_argument('--pages',type=int,default=6);parser.add_argument('--details',type=int,default=65);args=parser.parse_args()
    records=_read(ROOT/'data/collection/m5ware-candidates.json',{})
    for page in range(1,args.pages+1):
        url='https://m5ware.com/'+('' if page==1 else '?page='+str(page))
        try:
            response=fetch_public(url,offline=not args.online);links=Links();links.feed(response['body'].decode())
            for href,title in links.links:
                if not re.match(r'/projects/\d+',href):continue
                detail=urljoin(url,href.split('?')[0])
                entry=records.setdefault(detail,{'url':detail,'directoryTitle':title,'sourcePage':url,'status':'discovered'})
                if any(word in title for word in ['LIB Libraries','DOCS Guides & docs']):entry.update(status='deferred',reason='Framework/library/docs; applications prioritized')
            _write(ROOT/'data/collection/m5ware-candidates.json',records)
            print('M5Ware page',page,'candidates',len(records),flush=True)
        except (RuntimeError,Deferred) as error:print(error,flush=True)
    projects=_read(ROOT/'data/collection/project-candidates.json',{})
    count=0
    for url,record in records.items():
        if record['status']=='deferred':continue
        if record.get('repository'):
            repo=record['repository']
        else:
            if count>=args.details:break
            try:
                result=fetch_public(url,offline=not args.online);links=Links();links.feed(result['body'].decode())
                repos=[repo_from_url(href) for href,title in links.links if title=='View repository']
                repo=next((repo for repo in repos if repo),None)
                if not repo:
                    record.update(status='needs-review',reason='No upstream repository link');continue
                record.update(repository=repo,status='discovered',checkedAt=result['checkedAt'])
                count+=1
            except (RuntimeError,Deferred) as error:
                record.update(status='needs-review',reason=str(error));print(error,flush=True);continue
        entry=projects.setdefault(repo.lower(),{'repository':repo,'status':'discovered','discoveredAt':utc_now(),'sources':[],'reason':None})
        if url not in entry['sources']:entry['sources'].append(url)
        if not entry.get('directoryTitle'):entry['directoryTitle']=record['directoryTitle']
        entry.setdefault('m5wareDescription',record['directoryTitle'])
        _write(ROOT/'data/collection/project-candidates.json',projects)
        _write(ROOT/'data/collection/m5ware-candidates.json',records)
        print('Repository',repo,flush=True)
    print('Total repositories:',len(projects),flush=True)

if __name__=='__main__':main()
