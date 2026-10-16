"""Discover repository links from an already-cached directory README. No network."""
import argparse,re
from public_fetch import ROOT,_read,_write,fetch_public,utc_now
from discover import repo_from_url

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);args=p.parse_args()
 evidence=_read(ROOT/'data/collection/repository-evidence.json',{}).get(args.repo.lower(),{})
 if not evidence.get('readmeCacheUrl'):raise SystemExit('The directory README must already have been collected')
 body=fetch_public(evidence['readmeCacheUrl'],accept='application/vnd.github.raw+json',offline=True)['body'].decode(errors='replace')
 candidates=_read(ROOT/'data/collection/project-candidates.json',{});before=len(candidates)
 source='https://github.com/'+evidence['repository']
 for line in body.splitlines():
  for href in re.findall(r'https://github\.com/[\w.-]+/[\w.-]+(?:[^\s<>"\)]*)?',line):
   repo=repo_from_url(href)
   if not repo or repo.lower()==args.repo.lower():continue
   record=candidates.setdefault(repo.lower(),dict(repository=repo,status='discovered',discoveredAt=utc_now(),sources=[],reason=None))
   if source not in record['sources']:record['sources'].append(source)
   if not record.get('directoryDescription'):record['directoryDescription']=line.strip()
 _write(ROOT/'data/collection/project-candidates.json',candidates)
 print('Cached directory:',source,'added',len(candidates)-before,'candidates; total',len(candidates))
if __name__=='__main__':main()
