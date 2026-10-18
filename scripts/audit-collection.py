"""Milestone gate against the built catalog, raw MD identity, and intake evidence.
Run pnpm content:generate and pnpm collect:report before this command.
"""
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent/'collection'))
from public_fetch import ROOT,_read
from report import frontmatter
from intake_policy import star_threshold_exempt
p=argparse.ArgumentParser();p.add_argument('--min-projects',type=int,default=60);p.add_argument('--min-devices',type=int,default=40);args=p.parse_args()
catalog=_read(ROOT/'src/generated/catalog.json',{})
evidence=_read(ROOT/'data/collection/repository-evidence.json',{})
queue=_read(ROOT/'data/collection/queue.json',[])
errors=[]
projects=catalog.get('projects',[]);devices=catalog.get('devices',[])
if len(projects)<args.min_projects:errors.append(f'Projects: {len(projects)} < {args.min_projects}')
if len(devices)<args.min_devices:errors.append(f'Devices: {len(devices)} < {args.min_devices}')
for kind,entries in [('project',projects),('device',devices)]:
    published={entry['id'] for entry in entries}
    included=[r.get('content',{}).get('id') for r in queue if r['kind']==kind and r['status']=='included']
    if set(included)!=published:errors.append(f'{kind}: report included IDs differ from public catalog')
    if len(included)!=len(set(included)):errors.append(f'{kind}: report double-counts included records')
    md_ids={frontmatter(file).get('id') for file in (ROOT/f'content/{kind}s').rglob('*.md')}
    if published-md_ids:errors.append(f'{kind}: public IDs missing Markdown')
    for entry in entries:
        if not entry.get('sources'):errors.append(f'{entry["id"]}: no provenance sources')
        if set(entry.get('summary',{}))!={'en','zh','ja'}:errors.append(f'{entry["id"]}: missing translation')
for project in projects:
    repo=project['repository'].removeprefix('https://github.com/').lower()
    verified=next((e for e in evidence.values() if e.get('repository','').lower()==repo and e.get('status')=='verified'),None)
    if not verified:errors.append(f'{project["id"]}: no verified upstream evidence');continue
    if not verified.get('readmeCheckedAt') or verified.get('readmeCharacters',0)<50:errors.append(f'{project["id"]}: README not verified')
    metric=project.get('metrics',{})
    if metric.get('stars',-1)<0 or not metric.get('checkedAt') or (metric['stars']<10 and not star_threshold_exempt(ROOT,repo)):errors.append(f'{project["id"]}: no dated Star snapshot meeting the threshold or owner exemption')
    if metric.get('githubId')!=verified.get('githubId'):errors.append(f'{project["id"]}: GitHub identity mismatch')
    declared=(verified.get('license') or {}).get('spdx_id')
    label=verified.get('verifiedLicense') or (declared if declared and declared!='NOASSERTION' else 'Not specified')
    if project['license']!=label:errors.append(f'{project["id"]}: license differs from verified declaration')
    if verified.get('verifiedLicense') and not (verified.get('licenseReview',{}).get('sourceUrl') and verified.get('licenseReview',{}).get('checkedAt')):errors.append(f'{project["id"]}: manual license resolution lacks provenance')
    if project['devices'] and project['compatibility']!='documented':errors.append(f'{project["id"]}: linked models not marked documented')
if errors:
    print('Milestone audit incomplete:\n'+'\n'.join('- '+e for e in errors));raise SystemExit(1)
print(f'Collection milestone passed: {len(projects)} projects, {len(devices)} devices; all have MD, 3 languages, provenance; projects have verified README, recorded license facts and dated stars meeting the threshold or owner exemption; report counts agree.')
