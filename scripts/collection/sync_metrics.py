"""Refresh public repository metrics; anonymous, incremental, no failed-zero writes."""
import argparse,json
from public_fetch import fetch_public,_read,_write,ROOT,Deferred
from report import frontmatter

def main():
    p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');p.add_argument('--refresh',action='store_true');p.add_argument('--max',type=int,default=1000);args=p.parse_args()
    path=ROOT/'data/repository-metrics.json';metrics=_read(path,{})
    evidence=_read(ROOT/'data/collection/repository-evidence.json',{})
    count=0
    for file in sorted((ROOT/'content/projects').rglob('*.md')):
        if count>=args.max:break
        record=frontmatter(file)
        if not record.get('repository'):continue
        repo=record['repository'].removeprefix('https://github.com/')
        try:
            source=next((e.get('apiUrl') for e in evidence.values() if e.get('repository','').lower()==repo.lower() and e.get('apiUrl')), 'https://api.github.com/repos/'+repo)
            result=fetch_public(source,accept='application/vnd.github+json',ttl=0 if args.refresh else 86400,offline=not args.online)
            metadata=json.loads(result['body'])
            if metadata['full_name'].lower()!=repo.lower():
                print(file.name,'needs review: repository renamed to',metadata['full_name'],flush=True);continue
            previous=metrics.get(record['id'],{})
            if previous.get('githubId') is not None and previous['githubId']!=metadata['id']:
                raise RuntimeError('GitHub repository ID changed; review identity before replacing the snapshot')
            metrics[record['id']]={'repository':record['repository'],'githubId':metadata['id'],'stars':metadata['stargazers_count'],'checkedAt':result['checkedAt'],'pushedAt':metadata.get('pushed_at'),'archived':metadata.get('archived',False),'sourceUrl':result['url']}
            _write(path,metrics);count+=1
            print(record['id'],metadata['stargazers_count'],flush=True)
        except Deferred as error:
            print('Deferred; previous metrics preserved:',error,flush=True)
            if args.online:break
        except (RuntimeError,KeyError,json.JSONDecodeError) as error:
            print('Failed; previous metrics preserved:',record.get('id'),str(error),flush=True)
    print('Snapshots retained:',len(metrics),flush=True)

if __name__=='__main__':main()
