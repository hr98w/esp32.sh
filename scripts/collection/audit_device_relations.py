"""Offline model-name evidence audit. A text match is a review aid, never a hardware test."""
import re,json
from public_fetch import ROOT,_read,_write,fetch_public,Deferred,utc_now

ALIASES={
 'm5stack-basic':['M5Stack BASIC','M5Stack Basic','M5Stack Core ESP32','M5Core Basic'],
 'm5stack-cardputer':['M5Cardputer','Cardputer'],
 'm5stack-cardputer-adv':['Cardputer ADV','Cardputer-ADV','Cardputer_Adv','M5CardputerADV'],
 'm5stack-sticks3':['M5StickS3','StickS3','M5Stick S3'],
 'm5stack-stopwatch':['M5 StopWatch','M5Stack StopWatch','m5-stopwatch'],
 'm5stack-stackchan':['M5StackChan','official StackChan','K151'],
 'm5stack-dial':['M5Dial','M5 Dial'],
 'm5stack-stickc':['M5StickC','M5Stick C'],
 'm5stack-stickc-plus':['M5StickC Plus','M5Stick C Plus','StickCPlus'],
 'm5stack-stickc-plus2':['M5StickC Plus2','M5Stick C Plus2','StickCPlus2','StickC Plus2','StickC Plus/Plus2'],
 'lilygo-t3s3-v1-0':['T3 S3','T3-S3','T3S3'],
 'lilygo-lora32-oled':['LoRa32','LoRa 32'],
 'lilygo-t-watch-s3':['T-Watch S3','T-Watch-S3','TWatch-S3','TWatch S3'],
 'm5stack-paper':['M5Paper','M5 Paper'],
 'm5stack-fire':['M5Stack FIRE','M5Stack Fire','M5StackFire'],
 'm5stack-core2':['M5Core2','Core2'],
 'm5stack-cores3':['M5CoreS3','CoreS3'],
 'm5stack-atoms3':['AtomS3','ATOM S3'],
 'm5stack-atom-lite':['ATOM Lite','AtomLite'],
}
def normal(s):return re.sub(r'[^a-z0-9]','',s.lower())
def main():
 c=_read(ROOT/'src/generated/catalog.json',{});evidence=_read(ROOT/'data/collection/repository-evidence.json',{});devices={d['id']:d for d in c['devices']};out=[]
 manual={(r['projectId'],r['deviceId']):r for r in _read(ROOT/'data/collection/device-compatibility-review.json',{}).get('findings',[]) if r['status'].startswith('documented')}
 for p in c['projects']:
  e=next((e for e in evidence.values() if e.get('repository','').lower()==p['repository'].removeprefix('https://github.com/').lower()),{})
  try:body=fetch_public(e['readmeCacheUrl'],accept='application/vnd.github.raw+json',offline=True)['body'].decode(errors='replace')
  except (Deferred,KeyError):body=''
  for relation in p['devices']:
   d=devices[relation['deviceId']];aliases=ALIASES.get(d['id'],[d['name']]+d.get('aliases',[]))
   # V1.x labels remain a separate review concern, not matched as generic model names.
   matches=[line.strip() for line in body.splitlines() if any(normal(alias) in normal(line) for alias in aliases)]
   row={'projectId':p['id'],'deviceId':d['id'],'sourceUrl':relation['sourceUrl'],'readmeCheckedAt':e.get('readmeCheckedAt'),'status':'model-name-found' if matches else 'source-review-needed','context':matches[:3]}
   review=manual.get((p['id'],d['id']))
   if review and review['sourceUrl']==relation['sourceUrl']:
    row.update(status='source-context-reviewed',reviewBasis=review['basis'])
   if row['status']=='source-review-needed':print(p['id'],d['id'],relation['sourceUrl'])
   out.append(row)
 _write(ROOT/'data/collection/device-relation-audit.json',{'generatedAt':utc_now(),'scope':'All listed relations; offline lexical review aid only, not execution or hardware verification.','relations':out})
 print('Audited',len(out),'relations;',sum(r['status']=='source-review-needed' for r in out),'need source-context review')
if __name__=='__main__':main()
