"""Find a non-badge README image from already-cached, verified upstream READMEs.
No network calls; writes a separate derived snapshot. Manual covers always win.
"""
import html,re
from urllib.parse import urljoin,urlparse,quote,unquote
from public_fetch import ROOT,_read,_write,fetch_public,Deferred
from report import frontmatter

def images(body):
    # Preserve source order across Markdown and HTML image syntax.
    pattern=r'!\[[^\]]*\]\(\s*<?([^\s)>]+)>?(?:\s+[^)]*)?\)|<img\b[^>]*\bsrc=["\']([^"\']+)["\'][^>]*>'
    for match in re.finditer(pattern,body,re.I):yield html.unescape(match[1] or match[2])

def image_url(candidate,repo,branch):
    if any(word in candidate.lower() for word in ['badge','shields.io','travis-ci','actions/workflows','logo','opencollective','trendshift','buymeacoffee','donat','membrowse','discord']):return None
    if candidate.startswith(('data:','javascript:','http:','//')):return None
    base=f'https://raw.githubusercontent.com/{repo}/{quote(branch,safe="")}/'
    if candidate.startswith('/') and not candidate.startswith('//'):candidate=candidate.lstrip('/')
    url=urljoin(base,candidate)
    url=re.sub(r'https://github.com/([^/]+/[^/]+)/blob/',r'https://raw.githubusercontent.com/\1/',url)
    parsed=urlparse(url)
    if parsed.scheme!='https' or parsed.username or parsed.password:return None
    if parsed.hostname not in {'raw.githubusercontent.com','github.com','user-images.githubusercontent.com','github-production-user-asset-6210df.s3.amazonaws.com','img.youtube.com'}:return None
    if not re.search(r'\.(?:png|jpe?g|webp|gif)(?:[?#]|$)',url,re.I):return None
    return url

def main():
    evidence=_read(ROOT/'data/collection/repository-evidence.json',{})
    result={}
    for file in sorted((ROOT/'content/projects').rglob('*.md')):
        data=frontmatter(file)
        repo=data.get('repository','').removeprefix('https://github.com/')
        record=next((e for e in evidence.values() if e.get('repository','').lower()==repo.lower() and e.get('status')=='verified'),None)
        if not record:continue
        try:body=fetch_public(record['readmeCacheUrl'],accept='application/vnd.github.raw+json',offline=True)['body'].decode(errors='replace')
        except Deferred:continue
        for candidate in images(body):
            image=image_url(candidate,repo,record['defaultBranch'])
            if image:
                result[data['id']]={'repository':data['repository'],'url':image,'sourceUrl':'https://github.com/'+repo+'#readme','checkedAt':record['readmeCheckedAt']}
                break
    _write(ROOT/'data/repository-covers.json',result)
    print('README image candidates:',len(result),'(heuristic, name fallback on load failure)')
if __name__=='__main__':main()
