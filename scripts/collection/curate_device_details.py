"""Stage selected M5Stack facts from cached three-language official tables.
No network and no Markdown writes. Unaligned tables stay for manual review.
"""
import sys,json,re;sys.path.insert(0,'scripts/collection');from public_fetch import ROOT,_read,_write
E=_read(ROOT/'data/collection/device-enrichment-evidence.json',{});L=_read(ROOT/'data/collection/m5stack-localized-evidence.json',{})
# Hardware facts are selected, not whole manufacturer marketing descriptions.
priority=['SoC','Main Controller','Main Controller SoC','Wireless Module SoC','Flash','PSRAM','Display','Screen','IPS Display','IPS LCD Screen','IPS Screen','Touch IPS LCD','IPS LCD','LCD Screen','E-ink Screen','E-Ink Display','Resolution','TFT Driver IC','Screen Driver','Touch Driver','Touch Controller','Capacitive Touch IC','Camera','Image Sensor','Max Resolution','IMU','6-axis IMU','Motion Sensor','MEMS','3-axis Magnetometer','Microphone','Speaker','Speaker Setup','Audio Codec','Audio Chip','Human Interactions','Sensors','Keyboard','Encoder','RFID','Battery Capacity','Lithium Battery','Battery','Power','Power Input','Input Power','Power Supply','Input Voltage','USB Power','RS485 Power','Wide Voltage Input Range','Interface','Interfaces','Expansion Ports','Expansion Interface','Host Interface','Host Ports','Expansions','USB','USB Ports','Battery Port','Battery Socket Specification','Buttons','Button','Physical Buttons','RTC','RTC Clock Chip','Motors','Wi-Fi','Product Size','Product Weight']
# Devices with many peripherals get the key differences first, then dimensions.
custom={
'm5stack-coreink':{'E-Ink Display':{'zh':'1.54 英寸电子纸 · 200 × 200 · GDEW0154M09','en':'1.54-inch e-paper · 200 × 200 · GDEW0154M09','ja':'1.54インチ電子ペーパー · 200 × 200 · GDEW0154M09'}},
'm5stack-tab5':{'Display':{'zh':'5 英寸 IPS 触摸屏 · 1280 × 720 · ST7123 / ST7121','en':'5-inch IPS touchscreen · 1280 × 720 · ST7123 / ST7121','ja':'5インチIPSタッチ画面 · 1280 × 720 · ST7123 / ST7121'}},
}
def main_table(tables):
 return max(tables,key=lambda t:sum(len(r)==2 and r[0] in priority for r in t),default=[])
out=_read(ROOT/'data/collection/device-detail-review.json',{})
for id,e in E.items():
 if not id.startswith('m5stack-') or id=='m5stack-stopwatch':continue
 table=main_table(e['tables']);localized={l:main_table(L.get(id,{}).get(l,{}).get('tables',[])) for l in ['zh','ja']}
 # Do not align versions of a table that have added/removed rows.
 if any(len(t)!=len(table) for t in localized.values()):
  print('TABLE ALIGNMENT NEEDS REVIEW',id,len(table),{l:len(t) for l,t in localized.items()});continue
 selected=[key for key in priority if any(len(r)==2 and r[0]==key for r in table)]
 # Keep the page concise while retaining physical size and weight.
 selected=[k for k in selected if k not in {'Product Size','Product Weight'}][:13]+[k for k in ['Product Size','Product Weight'] if k in selected]
 specs=[];keys=[]
 for key in selected:
  index=next(i for i,r in enumerate(table) if len(r)==2 and r[0]==key)
  label={'en':key,**{l:localized[l][index][0] for l in localized}}
  values={'en':table[index][1],**{l:localized[l][index][1] for l in localized}}
  if key in custom.get(id,{}):values=custom[id][key]
  # Avoid copying long paragraphs into a technical facts table.
  if any(len(v)>230 for v in values.values()):continue
  specs.append({'label':label,'value':values});keys.append(key)
 resources=[]
 categories=[('Arduino',{'zh':'Arduino 入门','en':'Arduino quick start','ja':'Arduino入門'}),('uiflow2',{'zh':'UIFlow2 入门','en':'UIFlow2 quick start','ja':'UIFlow2入門'}),('Schematics',{'zh':'官方原理图','en':'Official schematic','ja':'公式回路図'}),('Factory',{'zh':'出厂固件资料','en':'Factory firmware resources','ja':'出荷時ファームウェア資料'})]
 for term,label in categories:
  found=next((r for r in e['resources'] if term.lower() in r['label'].lower() and (term!='Arduino' or '/arduino/' in r['url']) and (term!='Factory' or '/docs.' in r['url'] or 'docs.m5stack.com' in r['url'])),None)
  if found:resources.append({'label':label,'url':found['url']})
 sources=[{'url':e['sourceUrl'],'checkedAt':e['checkedAt']}]+[{'url':v['sourceUrl'],'checkedAt':v['checkedAt']} for v in L.get(id,{}).values() if 'sourceUrl' in v]
 out[id]={'specifications':specs,'resources':resources,'sources':sources,'reviewedFields':keys}
 print(id,len(specs),'facts;',', '.join(keys))
_write(ROOT/'data/collection/device-detail-review.json',out)
main_count=len(out);print('Prepared',main_count)
