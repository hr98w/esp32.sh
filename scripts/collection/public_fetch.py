"""Anonymous, cached, rate-aware GET requests. Never reads GitHub credentials."""
from __future__ import annotations
import fcntl
import hashlib
import json
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlparse, parse_qsl

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / '.cache' / 'collection'
USER_AGENT = 'esp32.sh-catalog/0.1 (anonymous public research; low-rate)'

class Deferred(RuntimeError):
    pass

def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')

def validate_url(url):
    parsed = urlparse(url)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('Only credential-free public HTTPS URLs are allowed')
    if any(key.lower() in {'token', 'access_token', 'api_key', 'apikey', 'auth', 'authorization'} for key, _ in parse_qsl(parsed.query)):
        raise ValueError('Authentication parameters are not allowed')
    return parsed

def _read(path, default):
    try: return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError): return default

def _write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)

def _curl(url, headers):
    with tempfile.TemporaryDirectory(prefix='esp32-public-get-') as temp:
        body, response_headers = Path(temp)/'body', Path(temp)/'headers'
        command = ['curl', '-q', '--proto', '=https', '--proto-redir', '=https', '--location', '--max-redirs', '3',
                   '--silent', '--show-error', '--connect-timeout', '10', '--max-time', '45',
                   '--user-agent', USER_AGENT, '--dump-header', str(response_headers), '--output', str(body), '--write-out', '%{http_code}']
        for key, value in headers.items():
            if key.lower() not in {'accept', 'if-none-match', 'if-modified-since'}: raise ValueError('Header not allowed')
            command += ['--header', f'{key}: {value}']
        result = subprocess.run(command + ['--url', url], capture_output=True, text=True)
        if result.returncode: raise RuntimeError(f'Anonymous request failed ({result.returncode}): {result.stderr.strip()}')
        blocks = response_headers.read_text(errors='replace').replace('\r\n', '\n').strip().split('\n\n')
        final = blocks[-1]
        parsed = dict((line.split(':', 1)[0].lower(), line.split(':', 1)[1].strip()) for line in final.splitlines()[1:] if ':' in line)
        return int(result.stdout[-3:]), parsed, body.read_bytes() if body.exists() else b''

def _fetch_public(url, *, accept='text/html', ttl=86400, offline=False, cache_dir=None):
    parsed = validate_url(url)
    directory = Path(cache_dir) if cache_dir else CACHE
    directory.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256((url+'\n'+accept).encode()).hexdigest()
    meta_path, body_path = directory/(key+'.json'), directory/(key+'.body')
    meta = _read(meta_path, {})
    now = time.time()
    if body_path.exists() and meta and (offline or now-meta.get('checkedEpoch', 0)<ttl):
        return {**meta, 'body': body_path.read_bytes(), 'cached': True}
    if offline: raise Deferred(f'Offline cache miss: {url}')
    state_path = directory/('request-state-'+hashlib.sha256(parsed.hostname.encode()).hexdigest()[:16]+'.json')
    legacy = _read(directory/'request-state.json', {})
    state = _read(state_path, legacy.get(parsed.hostname, {}))
    if state.get('blockedUntil', 0)>now:
        raise Deferred(f'{parsed.hostname} deferred until {datetime.fromtimestamp(state["blockedUntil"], timezone.utc).isoformat()}')
    delay = max(0, state.get('lastRequest', 0)+1.5-now)
    if delay: time.sleep(delay)
    request_headers = {'Accept': accept}
    if meta.get('etag'): request_headers['If-None-Match'] = meta['etag']
    status, headers, body = _curl(url, request_headers)
    state['lastRequest'] = time.time()
    remaining = headers.get('x-ratelimit-remaining')
    if remaining == '0': state['blockedUntil'] = float(headers.get('x-ratelimit-reset', time.time()+3600))+2
    if status in (403, 429):
        retry_after = headers.get('retry-after', '60')
        try: retry_seconds = float(retry_after)
        except ValueError:
            try: retry_seconds = parsedate_to_datetime(retry_after).timestamp() - time.time()
            except (TypeError, ValueError): retry_seconds = 60
        state['blockedUntil'] = max(state.get('blockedUntil', 0), time.time()+max(60,retry_seconds))
    _write(state_path, state)
    if status in (403, 429): raise Deferred(f'{status} from {parsed.hostname}; request paused, previous cache retained')
    if status == 304 and body_path.exists():
        meta.update({'checkedAt': utc_now(), 'checkedEpoch': time.time()})
        _write(meta_path, meta)
        return {**meta, 'body': body_path.read_bytes(), 'cached': True}
    if status != 200: raise RuntimeError(f'HTTP {status}: {url}')
    meta = {'url': url, 'status': status, 'checkedAt': utc_now(), 'checkedEpoch': time.time(), 'etag': headers.get('etag'), 'remaining': remaining}
    body_path.write_bytes(body)
    _write(meta_path, meta)
    return {**meta, 'body': body, 'cached': False}


def fetch_public(url, *, accept='text/html', ttl=86400, offline=False, cache_dir=None):
    # Serialize same-host requests across collector processes. Offline reads also
    # see complete atomic metadata rather than racing a concurrent revalidation.
    parsed = validate_url(url)
    directory = Path(cache_dir) if cache_dir else CACHE
    directory.mkdir(parents=True, exist_ok=True)
    lock_path = directory / ('host-' + hashlib.sha256(parsed.hostname.encode()).hexdigest()[:16] + '.lock')
    with lock_path.open('a') as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        try:
            return _fetch_public(url, accept=accept, ttl=ttl, offline=offline, cache_dir=directory)
        finally:
            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
