"""Rebuild a reviewable queue and coverage report from source ledgers and actual MD files."""
from intake_policy import star_threshold_exempt
import json,re
from collections import Counter,defaultdict
from pathlib import Path
from urllib.parse import urlparse
from public_fetch import ROOT,_read,_write,utc_now

def frontmatter(file):
    # JSON-format frontmatter used by generated records is directly readable here.
    text=file.read_text();match=re.match(r'---\n([\s\S]*?)\n---',text)
    if not match:return {}
    try:return json.loads(match[1])
    except json.JSONDecodeError:
        values={}
        for key in ['id','repository','name']:
            found=re.search(r'^'+key+r': (.*)$',match[1],re.M)
            if found:values[key]=found[1].strip('"\'')
        return values

def collapse_project_aliases(records):
    merged={}
    for record in records:
        canonical=record['repository'].lower()
        if canonical not in merged:
            merged[canonical]={**record,'discoveryKeys':[record['key']]}
        else:
            existing=merged[canonical]
            existing['sources']=list(dict.fromkeys(existing['sources']+record['sources']))
            existing['discoveryKeys'].append(record['key'])
            if record['status']=='included' and existing['status']!='included':
                sources,keys=existing['sources'],existing['discoveryKeys']
                merged[canonical]={**record,'sources':sources,'discoveryKeys':keys}
    return list(merged.values())

def source_label(url):
    parsed=urlparse(url);host=(parsed.hostname or '').removeprefix('www.')
    path=parsed.path.lower().rstrip('/')
    if host=='m5ware.com':return 'M5Ware'
    if host=='espboards.dev':return 'ESPboards'
    if host=='github.com' and path.startswith('/s0lness/awesome-esp32'):return 'awesome-esp32'
    if host=='github.com' and path.startswith('/terremoth/awesome-m5stack-cardputer'):return 'Awesome M5Stack Cardputer'
    if host in {'github.com','api.github.com'}:return 'Upstream project documentation'
    return 'Upstream manufacturer documentation'

def main():
    candidates=_read(ROOT/'data/collection/project-candidates.json',{})
    evidence=_read(ROOT/'data/collection/repository-evidence.json',{})
    devices=_read(ROOT/'data/collection/device-candidates.json',{})
    metrics=_read(ROOT/'data/repository-metrics.json',{})
    projects_on_disk={}
    devices_on_disk={}
    for file in (ROOT/'content/projects').rglob('*.md'):
        data=frontmatter(file)
        if data.get('repository'):projects_on_disk[data['repository'].lower().removeprefix('https://github.com/')]=dict(id=data['id'],file=str(file.relative_to(ROOT)))
    for file in (ROOT/'content/devices').glob('*/*.md'):
        data=frontmatter(file)
        if data.get('id'):devices_on_disk[data['id']]=dict(id=data['id'],file=str(file.relative_to(ROOT)),manufacturer=file.parent.name)
    reviewed={entry['data']['id']:entry['data'] for file in (ROOT/'data/collection').glob('reviewed-devices*.json') for entry in _read(file,[])}
    extras=_read(ROOT/'data/collection/additional-device-candidates.json',{})
    for suffix,id in [('devkitc1','espressif-esp32-s3-devkitc-1'),('cardputer','m5stack-cardputer')]:
        seed=_read(ROOT/f'data/collection/seed-device-{suffix}.json',{})
        reviewed[id]={'sources':[{'url':seed['url'],'checkedAt':seed.get('checkedAt')}]} if seed.get('url') else {}
        if seed.get('directoryUrl') in devices:devices[seed['directoryUrl']]['contentId']=id
    queue=[]
    for key,candidate in candidates.items():
        verified=evidence.get(key,{})
        if verified.get('status')=='alias':verified=evidence.get(verified.get('aliasOf'),verified)
        canonical=verified.get('repository',candidate['repository']).lower()
        included=projects_on_disk.get(canonical) or projects_on_disk.get(key)
        status='included' if included and verified.get('status')=='verified' else 'pending' if included else {'verified':'pending','excluded':'excluded','needs-review':'needs-review','pending':'pending'}.get(verified.get('status'),'discovered')
        snapshot=metrics.get(included['id'],{}) if included else {}
        low_stars=isinstance(snapshot.get('stars'),int) and snapshot['stars']<10 and not star_threshold_exempt(ROOT, canonical)
        if low_stars:status='needs-review'
        queue.append({'kind':'project','key':key,'repository':verified.get('repository',candidate['repository']),'status':status,'content':included,'sources':candidate['sources'],'stars':snapshot.get('stars',verified.get('stars')),'checkedAt':snapshot.get('checkedAt',verified.get('starsCheckedAt')),'reason':('Latest confirmed stars below 10; hidden from public catalog, Markdown retained' if low_stars else verified.get('reason')) or ('Verified upstream; summaries and device mapping pending' if verified.get('status')=='verified' and not included else 'Upstream verification pending' if not verified else None)})
    queue=collapse_project_aliases(queue)
    known_repositories={record['repository'].lower() for record in queue if record['kind']=='project'}
    for key,included in projects_on_disk.items():
        if key not in known_repositories:
            queue.append({'kind':'project','key':key,'repository':key,'status':'pending','content':included,'sources':[],'reason':'Existing seed; fresh README, license and Star verification pending'})
    for url,candidate in devices.items():
        details=candidate.get('details',{})
        included=devices_on_disk.get(candidate.get('contentId',candidate['id']))
        queue.append({'kind':'device','key':url,'id':candidate.get('contentId',candidate['id']),'name':details.get('name'),'manufacturer':details.get('manufacturer',{}).get('id',candidate.get('manufacturerHint','unknown')),'status':'included' if included else 'needs-review' if details.get('primaryStatus')=='needs-review' else candidate.get('status','discovered'),'content':included,'sources':[url]+([details['officialUrl']] if details.get('officialUrl') else []),'reason':None if included else details.get('primaryReason') or candidate.get('reason','Device facts pending')})
    for record in queue:
        if record['kind']=='device' and record['status']!='included' and record['id'] in reviewed:
            record.update(status='pending',reason='Official facts and three-language summary reviewed; staged for publication')
    tracked_devices={record['id'] for record in queue if record['kind']=='device'}
    for id,data in reviewed.items():
        if id in tracked_devices or id in devices_on_disk:continue
        if not data.get('manufacturer'):continue
        queue.append({'kind':'device','key':id,'id':id,'name':data.get('name'),'manufacturer':data['manufacturer']['id'],'status':'pending','content':None,'sources':[source['url'] for source in data.get('sources',[])],'reason':'Official facts and multilingual summary staged; not published yet'})
        tracked_devices.add(id)
    for key,included in devices_on_disk.items():
        if key not in tracked_devices:queue.append({'kind':'device','key':key,'id':key,'manufacturer':included['manufacturer'],'status':'included','content':included,'sources':[s['url'] for s in reviewed.get(key,{}).get('sources',[])],'reason':None})
    for id,record in extras.items():
        if id in devices_on_disk:record.update(status='included',reason=None,content=devices_on_disk[id])
    _write(ROOT/'data/collection/additional-device-candidates.json',extras)
    _write(ROOT/'data/collection/queue.json',queue)
    counts={kind:dict(Counter(record['status'] for record in queue if record['kind']==kind)) for kind in ['project','device']}
    maker_counts=defaultdict(Counter)
    for record in queue:
        if record['kind']=='device':maker_counts[record['manufacturer']][record['status']]+=1
    source_counts={kind:defaultdict(Counter) for kind in ['project','device']}
    for record in queue:
        urls=record['sources'] if record['kind']=='project' else record['sources'][:1]
        for label in set(source_label(url) for url in urls):source_counts[record['kind']][label][record['status']]+=1
    staged_devices=sum(id not in devices_on_disk and bool(data.get('manufacturer')) for id,data in reviewed.items())
    snapshot={'stagedDevices':staged_devices,'sourceCoverage':source_counts,'generatedAt':utc_now(),'counts':counts,'manufacturerCoverage':dict(sorted(maker_counts.items())),'authorization':'Anonymous public GET only; no gh, personal keys, cookies, deployment or external writes'}
    _write(ROOT/'data/collection/progress.json',snapshot)
    lines=['# Collection progress','',f'Generated: {snapshot["generatedAt"]}','', 'This report is generated by `python3 scripts/collection/report.py`. Counts refer to discovered sources, not the complete ESP32 ecosystem.','', '## Records','', '| Kind | Included | Pending | Needs review | Discovered | Excluded |','| --- | ---: | ---: | ---: | ---: | ---: |']
    for kind,values in counts.items():lines.append('| '+kind+' | '+' | '.join(str(values.get(status,0)) for status in ['included','pending','needs-review','discovered','excluded'])+' |')
    lines += ['', f"Prepared device records awaiting publication: **{staged_devices}** (a subset of pending, not included)."]
    lines += ['', '## Discovery source coverage', '', 'One record can belong to multiple discovery sources. Source memberships must not be added together as a unique-project total. Raw repository aliases are merged before counting.', '', '| Kind / source | Included | Pending | Needs review | Discovered | Excluded |', '| --- | ---: | ---: | ---: | ---: | ---: |']
    for kind,groups in source_counts.items():
        for label,values in sorted(groups.items()):lines.append('| '+kind+' / '+label+' | '+' | '.join(str(values.get(status,0)) for status in ['included','pending','needs-review','discovered','excluded'])+' |')
    lines += ['', '## Manufacturer coverage','','| Manufacturer | Included | Pending | Needs review | Discovered |','| --- | ---: | ---: | ---: | ---: |']
    for maker,values in sorted(maker_counts.items()):lines.append('| '+maker+' | '+' | '.join(str(values.get(status,0)) for status in ['included','pending','needs-review','discovered'])+' |')
    inventories=_read(ROOT/'data/collection/manufacturer-inventory.json',{})
    lines += ['', '## ESPboards source coverage', '', 'The denominator below is the inspected manufacturer directory, not every device the manufacturer sells. Additional devices discovered through other sources are counted separately.', '', '| Manufacturer source | Listed in source | Included from source | Additional included | Checked |', '| --- | ---: | ---: | ---: | --- |']
    for maker,inventory in sorted(inventories.items()):
        source_records=[r for r in queue if r['kind']=='device' and r['manufacturer']==maker and r['key'] in devices]
        included_from_source=sum(r['status']=='included' for r in source_records)
        additional=maker_counts[maker].get('included',0)-included_from_source
        lines.append(f"| [{maker}]({inventory['sourceUrl']}) | {inventory.get('discoveredBoards',0)} | {included_from_source} | {additional} | {inventory.get('checkedAt','')} |")
    lines += ['', 'Full device-by-device states and reasons: [Device intake queue](device-intake-queue.md).', '']
    device_lines=['# Device intake queue', '', f"Generated: {snapshot['generatedAt']}", '', 'Included means an actual Markdown record exists. Pending or needs-review entries are not published. Source coverage is limited to inspected directories; model support is maintained separately on projects.', '']
    for maker in sorted(maker_counts):
        device_lines += [f'## {maker}', '', '| Device | Stable ID | Status | Reason |', '| --- | --- | --- | --- |']
        for record in sorted((r for r in queue if r['kind']=='device' and r['manufacturer']==maker),key=lambda r:(r['status'],r['id'])):
            name=(record.get('name') or record['id']).replace('|','/')
            if record['sources']:name=f"[{name}]({record['sources'][0]})"
            device_lines.append(f"| {name} | `{record['id']}` | {record['status']} | {str(record.get('reason') or '').replace('|','/')} |")
        device_lines.append('')
    (ROOT/'docs/research/device-intake-queue.md').write_text('\n'.join(device_lines)+'\n')
    lines += ['','## Project review queue','','| Repository | Stars | Status | Reason |','| --- | ---: | --- | --- |']
    for record in queue:
        if record['kind']=='project' and record['status']!='included':lines.append('| '+record['repository']+' | '+str(record.get('stars') if record.get('stars') is not None else '—')+' | '+record['status']+' | '+str(record.get('reason') or '').replace('|','/')+' |')
    (ROOT/'docs/research/collection-progress.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(counts,ensure_ascii=False))

if __name__=='__main__':main()
