"""Inspect manufacturer pages already linked from ESPboards; stage evidence, never auto-publish."""
import argparse,re
from urllib.parse import urlparse
from public_fetch import ROOT,_read,_write,fetch_public,Deferred
from discover import Links
from discover_devices import clean

def products(value):
 if isinstance(value,dict):
  if value.get('@type') in {'Product','ProductGroup'}:yield value
  for item in value.values():yield from products(item)
 elif isinstance(value,list):
  for item in value:yield from products(item)

def main():
 p=argparse.ArgumentParser();p.add_argument('--online',action='store_true');args=p.parse_args()
 rows=_read(ROOT/'data/collection/device-candidates.json',{});output=_read(ROOT/'data/collection/lilygo-variant-source-review.json',{})
 for record in rows.values():
  if record.get('manufacturerHint')!='lilygo' or record.get('contentId'):continue
  body=fetch_public(record['sourceUrl'],offline=True)['body'].decode();links=Links();links.feed(body)
  urls=[href for href,label in links.links if urlparse(href).hostname in {'lilygo.cc','www.lilygo.cc','wiki.lilygo.cc'}]
  url=next(iter(dict.fromkeys(urls)),None)
  if not url:continue
  # Store tracking parameters are not needed to inspect the product.
  url=url.split('?')[0]
  try:
   r=fetch_public(url,offline=not args.online);body=r['body'].decode();parser=Links();parser.feed(body)
   product=next((p for block in parser.jsonld for p in products(block)),{})
   text=clean(re.sub(r'<(?:script|style)[^>]*>[\s\S]*?</(?:script|style)>',' ',body))
   description=clean(product.get('description',''))
   if 'Shipping to worldwide' in text:text=text[text.index('Shipping to worldwide'):]
   title=re.search(r'<title[^>]*>(.*?)</title>',body,re.S)
   row=dict(id=record['id'],url=url,checkedAt=r['checkedAt'],sourceUrl=record['sourceUrl'],name=product.get('name'),title=clean(title[1]) if title else '',description=description,excerpt=text[:7000],status='needs-review')
   output[record['id']]=row
   print(record['id'],row['title'],flush=True)
  except (RuntimeError,Deferred) as error:
   output[record['id']]=dict(id=record['id'],url=url,status='needs-review',reason=str(error));print(record['id'],error,flush=True)
  _write(ROOT/'data/collection/lilygo-variant-source-review.json',output)
if __name__=='__main__':main()
