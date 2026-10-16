"""Verify explicitly reviewed replacement source URLs without mutating the discovery ledger."""
import argparse,re
from public_fetch import ROOT,_read,_write,fetch_public,Deferred
from discover_devices import clean

def main():
 p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');args=p.parse_args()
 output={}
 for id,source in _read(ROOT/'data/collection/device-source-overrides.json',{}).items():
  try:
   r=fetch_public(source['url'],offline=not args.online);body=r['body'].decode(errors='replace')
   article=re.search(r'<article[^>]*>([\s\S]*?)</article>',body)
   content=article[1] if article else body
   text=clean(re.sub(r'<(?:script|style)[^>]*>[\s\S]*?</(?:script|style)>',' ',content))
   title=re.search(r'<title[^>]*>(.*?)</title>',body,re.S)
   output[id]=dict(url=source['url'],checkedAt=r['checkedAt'],reason=source['reason'],title=clean(title[1]) if title else '',excerpt=text[:1000])
   print(id,output[id]['title'],flush=True)
  except (RuntimeError,Deferred) as error:print(id,error,flush=True)
 _write(ROOT/'data/collection/device-override-evidence.json',output)
if __name__=='__main__':main()
