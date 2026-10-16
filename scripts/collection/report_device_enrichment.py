"""Offline completeness ledger for every listed device, including blocked sources.

Completeness means sourced editorial coverage, not a hardware test or a promise
that every vendor specification has been transcribed.
"""
from collections import Counter
from public_fetch import ROOT, _read, _write, utc_now


def main():
    catalog = _read(ROOT/'src/generated/catalog.json', {})
    images = _read(ROOT/'data/collection/device-image-review.json', {})
    details = _read(ROOT/'data/collection/device-detail-review.json', {})
    rows = []
    for d in catalog['devices']:
        image = images.get(d['id'], {})
        detail = details.get(d['id'], {})
        pending = []
        if not d.get('cover'):
            pending.append({'task': 'official-image', 'reason': image.get('reason', 'No reviewed manufacturer image yet.')})
        elif image.get('status') != 'verified' or image.get('imageUrl') != d['cover']:
            raise SystemExit(f"{d['id']}: published image lacks matching verification")
        if not d.get('specifications'):
            pending.append({'task': 'primary-specifications', 'reason': detail.get('reason', 'Manufacturer documents moved; primary specifications need confirmation.')})
        if not d.get('resources'):
            pending.append({'task': 'resources', 'reason': 'No model-specific resource links.'})
        rows.append({'deviceId': d['id'], 'manufacturer': d['manufacturer']['id'],
                     'type': d['type'], 'status': 'pending' if pending else 'complete',
                     'image': bool(d.get('cover')), 'specifications': bool(d.get('specifications')),
                     'resources': bool(d.get('resources')), 'pending': pending,
                     'sources': d['sources']})
    result = {'generatedAt': utc_now(), 'scope': 'All listed devices; sourced key facts, not exhaustive transcription or physical testing.',
              'counts': {'devices': len(rows), 'complete': sum(r['status']=='complete' for r in rows),
                         'images': sum(r['image'] for r in rows), 'specifications': sum(r['specifications'] for r in rows),
                         'resources': sum(r['resources'] for r in rows)}, 'devices': rows}
    _write(ROOT/'data/collection/device-enrichment-queue.json', result)
    lines = ['# Device enrichment coverage', '', 'Generated: '+result['generatedAt'], '',
             'Every listed device is accounted for below. Complete means an externally hosted, reviewed manufacturer image, key sourced hardware specifications, and resource links. It does not mean exhaustive specifications or physical testing.', '',
             '| Manufacturer | Devices | Images | Key specifications | Resources | Complete |',
             '| --- | ---: | ---: | ---: | ---: | ---: |']
    for maker in sorted({r['manufacturer'] for r in rows}):
        group = [r for r in rows if r['manufacturer']==maker]
        lines.append(f"| {maker} | {len(group)} | {sum(r['image'] for r in group)} | {sum(r['specifications'] for r in group)} | {sum(r['resources'] for r in group)} | {sum(r['status']=='complete' for r in group)} |")
    lines += ['', '## Pending', '', '| Device | Task | Reason |', '| --- | --- | --- |']
    for r in rows:
        for task in r['pending']:
            lines.append(f"| {r['deviceId']} | {task['task']} | {task['reason'].replace('|', '/')} |")
    types = Counter(r['type'] for r in rows)
    lines += ['', '## Classification', '']+[f'- {t}: {n}' for t,n in sorted(types.items())]
    integrated = [r for r in rows if r['type']=='integrated-device']
    lines += ['', f"Integrated devices: {len(integrated)}; complete: {sum(r['status']=='complete' for r in integrated)}.", '',
              'Source ledgers: `device-image-review.json`, `device-detail-review.json`, and per-device Markdown. Run `python3 scripts/collection/report_device_enrichment.py` after generating the catalog.', '']
    (ROOT/'docs/research/device-enrichment-progress.md').write_text('\n'.join(lines))
    print(result['counts'])


if __name__=='__main__':
    main()
