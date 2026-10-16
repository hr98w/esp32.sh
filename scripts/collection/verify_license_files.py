"""Collect actual GitHub LICENSE files for manual resolution of conflicting/unknown metadata.
Default offline. This records evidence and never automatically approves a license.
"""
import argparse,base64,json,re,hashlib,time
from datetime import datetime,timezone
from public_fetch import ROOT,CACHE,_read,_write,fetch_public,Deferred,utc_now

def main():
 p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');p.add_argument('--repo',action='append',required=True);p.add_argument('--wait',action='store_true');p.add_argument('--deadline');args=p.parse_args()
 if args.wait:
  if not args.online or not args.deadline:raise SystemExit('--wait requires --online and an explicit --deadline')
  deadline=datetime.fromisoformat(args.deadline).timestamp();state_path=CACHE/('request-state-'+hashlib.sha256(b'api.github.com').hexdigest()[:16]+'.json')
  while time.time()<deadline:
   blocked=_read(state_path,{}).get('blockedUntil',0)
   if blocked<=time.time():break
   print(utc_now(),'license evidence waiting until',datetime.fromtimestamp(blocked,timezone.utc).isoformat(),flush=True)
   time.sleep(min(45,blocked-time.time(),deadline-time.time()))
  if time.time()>=deadline:raise SystemExit('Local deadline reached; no new license requests made')
 evidence=_read(ROOT/'data/collection/repository-evidence.json',{});path=ROOT/'data/collection/license-file-evidence.json';out=_read(path,{})
 for requested in args.repo:
  key=requested.lower();record=evidence.get(key)
  if not record:print('Not a collected repository:',requested,flush=True);continue
  repo=record['repository'];url='https://api.github.com/repos/'+repo+'/license'
  try:
   r=fetch_public(url,accept='application/vnd.github+json',offline=not args.online);value=json.loads(r['body']);text=base64.b64decode(value['content']).decode(errors='replace')
   local=ROOT/'.cache/collection'/('license-'+key.replace('/','--')+'.txt');local.write_text(text)
   out[key]={'repository':repo,'status':'fetched','url':url,'htmlUrl':value['html_url'],'path':value['path'],'sha':value['sha'],'detectedLicense':value.get('license'),'checkedAt':r['checkedAt'],'preamble':text[:220]}
   print('\nLICENSE FILE',repo,value['path'],(value.get('license') or {}).get('spdx_id'),'\n',text[:850],flush=True)
   lines=[line.strip() for line in text.splitlines() if re.search(r'non.?commercial|commons clause|commercial use|must not|shall not|not permitted',line,re.I)]
   if lines:print('Restriction phrases for review:',lines[:12],flush=True)
  except Deferred as error:print('Deferred; previous license evidence retained:',error,flush=True);break
  except (RuntimeError,KeyError,ValueError,json.JSONDecodeError) as error:
   if key in out:out[key].update(lastError=str(error),lastAttemptAt=utc_now())
   else:out[key]={'repository':repo,'status':'needs-review','reason':str(error),'lastAttemptAt':utc_now()}
   print(repo,error,flush=True)
  _write(path,out)
if __name__=='__main__':main()
