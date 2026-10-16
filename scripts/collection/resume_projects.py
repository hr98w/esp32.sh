"""Wait for recorded GitHub reset times, then resume anonymous verification.
This is a local operator command, never a deployed/background website task.
"""
import argparse,hashlib,subprocess,time
from datetime import datetime,timezone
from public_fetch import ROOT,CACHE,_read,utc_now

def main():
 p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');p.add_argument('--target',type=int,default=65);p.add_argument('--deadline',required=True);args=p.parse_args()
 deadline=datetime.fromisoformat(args.deadline).timestamp()
 if not args.online:raise SystemExit('Explicit --online required; this command waits and performs anonymous requests')
 state_path=CACHE/('request-state-'+hashlib.sha256(b'api.github.com').hexdigest()[:16]+'.json')
 while time.time()<deadline:
  evidence=_read(ROOT/'data/collection/repository-evidence.json',{})
  verified=sum(e.get('status')=='verified' for e in evidence.values())
  if verified>=args.target:print('Verification target reached:',verified,flush=True);return
  state=_read(state_path,{})
  blocked=state.get('blockedUntil',0)
  if blocked>time.time():
   print(utc_now(),'waiting for API reset',datetime.fromtimestamp(blocked,timezone.utc).isoformat(),'verified',verified,flush=True)
   time.sleep(min(45,blocked-time.time(),deadline-time.time()));continue
  before=len(evidence),verified
  result=subprocess.run(['python3','scripts/collection/verify_projects.py','--online','--max',str(min(60,args.target-verified))],cwd=ROOT)
  if result.returncode:raise SystemExit(result.returncode)
  after=_read(ROOT/'data/collection/repository-evidence.json',{})
  if (len(after),sum(e.get('status')=='verified' for e in after.values()))==before and _read(state_path,{}).get('blockedUntil',0)<=time.time():
   print('No verification progress; inspect pending network errors, remaining candidates, or manual review before retrying.',flush=True);return
 print('Local deadline reached; progress is preserved.',flush=True)
if __name__=='__main__':main()
