"""Validate manually selected external images with anonymous, cached GETs."""
import argparse
from urllib.parse import quote
from public_fetch import ROOT,fetch_public,_read,_write,Deferred

def image_format(body):
 if body.startswith(b'\xff\xd8\xff'):return 'jpeg'
 if body.startswith(b'\x89PNG\r\n\x1a\n'):return 'png'
 if body.startswith((b'GIF87a',b'GIF89a')):return 'gif'
 if body.startswith(b'RIFF') and body[8:12]==b'WEBP':return 'webp'
 return None

def main():
 p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');args=p.parse_args()
 path=ROOT/'data/collection/device-image-review.json';records=_read(path,{})
 for id,r in records.items():
  if r['status']!='selected':continue
  url=quote(r['imageUrl'],safe=':/?&=%#@+;,!~*\'()')
  try:
   result=fetch_public(url,accept='image/*',offline=not args.online)
   fmt=image_format(result['body'])
   if not fmt:raise RuntimeError('Response is not a supported raster image')
   r.pop('reason',None)
   r.update(status='verified',imageUrl=url,format=fmt,bytes=len(result['body']),imageCheckedAt=result['checkedAt'])
   print(id,fmt,len(result['body']),flush=True)
  except (RuntimeError,Deferred) as error:r.update(status='needs-review',reason=str(error));print(id,error,flush=True)
  _write(path,records)
if __name__=='__main__':main()
