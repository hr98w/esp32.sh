"""Small read-only deployment smoke check; full local checks live in check-http.py.

Uses anonymous curl GETs with normal TLS validation. No credentials, browser,
upstream GitHub calls, or deployment mutations. Expected counts come from the
local generated catalog, which should match the version just built/deployed.
"""
import argparse
import json
import re
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, body):
        super().__init__()
        self.lang = None
        self.cards = 0
        self.headings = set()
        self.assets = []
        self.feed(body)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'html':
            self.lang = values.get('lang')
        if 'project-card' in values.get('class', '').split():
            self.cards += 1
        if tag == 'h2' and values.get('id'):
            self.headings.add(values['id'])
        asset = values.get('src') if tag == 'script' else values.get('href') if tag == 'link' else None
        if asset and asset.startswith('/assets/'):
            self.assets.append(asset)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base_url', nargs='?', default='https://esp32.sh')
    parser.add_argument('--delay', type=float, default=1, help='Seconds between GETs (default: 1)')
    parser.add_argument('--output', type=Path, default=ROOT/'.cache/deployment/public-smoke-results.json')
    args = parser.parse_args()
    base = args.base_url.rstrip('/')
    url = urlsplit(base)
    local = url.hostname in {'localhost', '127.0.0.1', '::1'}
    if not url.hostname or url.username or url.password or url.query or url.fragment or url.path:
        parser.error('Use a credential-free origin URL without path, query, or fragment.')
    if url.scheme != 'https' and not (local and url.scheme == 'http'):
        parser.error('Public checks require HTTPS; HTTP is allowed only for loopback previews.')
    if args.delay < 0:
        parser.error('--delay must not be negative.')
    catalog_path = ROOT/'src/generated/catalog.json'
    if not catalog_path.exists():
        parser.error('Generate the local catalog first: pnpm content:generate')
    catalog = json.loads(catalog_path.read_text())
    projects, devices = catalog['projects'], catalog['devices']
    if not projects or not devices:
        parser.error('The local catalog needs at least one project and one device.')
    by_id = {d['id']: d for d in devices}
    # Stable representative devices, with a fallback if future catalog scope changes.
    examples = [by_id.get('m5stack-stopwatch', devices[0]), by_id.get('seeed-reterminal-e1002', devices[-1])]
    filtered_id = examples[0]['id']
    filtered_count = sum(any(d['deviceId'] == filtered_id for d in p['devices']) for p in projects)
    checks = [('/', 'en', min(24,len(projects))), ('/zh', 'zh-CN', min(24,len(projects))),
              ('/ja', 'ja', min(24,len(projects))), ('/devices', 'en', min(24,len(devices))),
              ('/zh/devices/'+examples[0]['id'], 'zh-CN', None),
              ('/ja/devices/'+examples[1]['id'], 'ja', None),
              ('/?device='+filtered_id, 'en', min(24,filtered_count))]
    if len(projects)>24: checks.append(('/?page=2','en',min(24,len(projects)-24)))
    if len(devices)>24: checks.append(('/devices?page=2','en',min(24,len(devices)-24)))
    results = []
    with tempfile.TemporaryDirectory(prefix='esp32-deployment-check-') as temp:
        def get(path):
            if results:
                time.sleep(args.delay)
            body, headers = Path(temp)/'body', Path(temp)/'headers'
            command = ['curl', '-q', '--silent', '--show-error', '--fail', '--proto', '=http,https',
                       '--connect-timeout', '10', '--max-time', '30', '--dump-header', str(headers),
                       '--output', str(body), '--write-out', '%{http_code}', '--url', base+path]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(f'{path}: {result.stderr.strip()}')
            if result.stdout != '200':
                raise RuntimeError(f'{path}: expected HTTP 200, got {result.stdout}')
            content_types = re.findall(r'^content-type:\s*([^\r\n]+)', headers.read_text(), re.I | re.M)
            content_type = content_types[-1] if content_types else ''
            data = body.read_bytes()
            results.append({'url': base+path, 'status': 200, 'bytes': len(data), 'contentType': content_type})
            print(f'{path}: 200 ({len(data)} bytes)', flush=True)
            return data.decode(errors='replace'), content_type

        root = None
        for path, lang, count in checks:
            body, content_type = get(path)
            page = Page(body)
            if 'text/html' not in content_type or page.lang != lang:
                raise RuntimeError(f'{path}: expected HTML language {lang}, got {page.lang}')
            if count is not None and page.cards != count:
                raise RuntimeError(f'{path}: expected {count} cards from local catalog, got {page.cards}')
            if '/devices/' in path and 'related-projects' not in page.headings:
                raise RuntimeError(f'{path}: missing related-projects section')
            if '/devices/' in path:
                device = by_id[path.rsplit('/', 1)[-1]]
                locale = {'en': 'en', 'zh-CN': 'zh', 'ja': 'ja'}[lang]
                rendered = unescape(body)
                if device['name'] not in rendered or device['summary'][locale] not in rendered:
                    raise RuntimeError(f'{path}: detail content differs from the local catalog')
            if path == '/':
                root = page
        for suffix, mime in [('.css', 'text/css'), ('.js', 'javascript')]:
            assets = [a for a in root.assets if a.endswith(suffix)]
            if not assets:
                raise RuntimeError(f'Homepage has no {suffix} asset')
            asset = next((a for a in assets if '/index-' in a), assets[0])
            _, content_type = get(asset)
            if mime not in content_type:
                raise RuntimeError(f'{asset}: unexpected Content-Type {content_type}')

    snapshot = {'checkedAt': datetime.now(timezone.utc).isoformat(timespec='seconds'),
                'scope': 'Read-only HTTP/HTML and asset checks; no browser hydration or hardware validation.',
                'expected': {'projects': len(projects), 'devices': len(devices)}, 'results': results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2)+'\n')
    print(f'Passed {len(results)} deployment checks. Report: {args.output}')


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as error:
        raise SystemExit(str(error)) from error
