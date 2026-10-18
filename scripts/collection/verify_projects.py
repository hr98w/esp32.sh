"""Verify discovered repositories with anonymous GitHub REST requests, no credentials."""
import argparse,json,re
from public_fetch import fetch_public,_read,_write,ROOT,utc_now,Deferred


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--online',action='store_true');parser.add_argument('--max',type=int,default=60);parser.add_argument('--repo',action='append');parser.add_argument('--retry-review',action='store_true');args=parser.parse_args()
    candidates=_read(ROOT/'data/collection/project-candidates.json',{})
    evidence_path=ROOT/'data/collection/repository-evidence.json';evidence=_read(evidence_path,{})
    selected=[(repo,candidate) for repo,candidate in candidates.items() if not args.repo or repo in [r.lower() for r in args.repo]]
    seed_priority=['brucedevices/firmware','m5stack/m5cardputer-userdemo','justcallmekoko/esp32marauder','bmorcelli/launcher','stack-chan/stack-chan','m5stack/stackchan','echo-lalia/microhydra','haswitchplate/openhasp','landonr/homething','gkoh/furble','geo-tp/cardputer-game-station-emulators']
    # Prioritize existing device-specific discoveries before legacy SDK/library entries.
    seed_priority = ['trentct/m5stack-stopwatch-avatar', 'hanminyin/vibestick-for-mac', 'juicecultus/crosspoint-reader-papers3', 'geo-tp/bluetooth-keyboard-mouse-emulator', 'm5stack/m5dial-userdemo', 'koenvervloesem/m5stack-air-quality-esphome', 'ayutaz/sanotts-jp', 'volosr/m5cardremote', 'megabitsenmzq/esp32-homekit-remote', 'fernandofatech/tool-m5cardputer-sshclient', 'nishad2m8/pdaputer', 'geo-tp/retro-zero', 'incursiohack/esp-game-server', 'aat440hz/sshclient-m5cardputer'] + seed_priority
    # Balance the next batch with non-M5 projects already discovered in awesome-esp32.
    seed_priority += ['northstrix/midbar','doublemarkpro/homeworktimer-esp32-s3-touch-lcd-3.49','seichris/open-bike-computer','aideahandesen-dvs/tempmeter','khlebobul/esp_ble_finder','curisama/the-badge','rmno21/esp32-calculator','lpolasek/openrunn','khlebobul/esp_pomodoro_timer','esphome/esphome','openai/openai-realtime-embedded','s-iwaki-d/esp32drop','micropython/micropython','espressif/esp-idf','esp-rs/esp-hal']
    selected.sort(key=lambda item: (seed_priority.index(item[0]) if item[0] in seed_priority else 50 if any('m5ware.com' in str(source) for source in item[1].get('sources',[])) else 100, -int((re.search(r'([\d,]+)\s+stars', item[1].get('m5wareDescription','')) or [None,'0'])[1].replace(',','')), item[0]))
    processed=0
    for key,candidate in selected:
        if processed>=args.max:break
        if evidence.get(key,{}).get('status') in ({'verified','excluded','alias'} if args.retry_review else {'verified','excluded','needs-review','alias'}):continue
        repo=candidate['repository'];record=evidence.setdefault(key,{'repository':repo,'status':'pending'})
        try:
            result=fetch_public('https://api.github.com/repos/'+repo,accept='application/vnd.github+json',offline=not args.online)
            metadata=json.loads(result['body'])
            record.update(repository=metadata['full_name'],githubId=metadata['id'],stars=metadata['stargazers_count'],starsCheckedAt=result['checkedAt'],description=metadata.get('description'),archived=metadata.get('archived',False),defaultBranch=metadata['default_branch'],pushedAt=metadata.get('pushed_at'),apiUrl=result['url'],topics=metadata.get('topics',[]),license=metadata.get('license',{}))
            prior=next(((old_key,old) for old_key,old in evidence.items() if old_key!=key and old.get('githubId')==metadata['id'] and old.get('readmeCacheUrl') and old.get('status')!='alias'),None)
            if prior:
                record.update(status='alias',aliasOf=prior[0],reason='Canonical GitHub repository already tracked; discovery sources are merged in the report')
                _write(evidence_path,evidence);processed+=1
                print(repo,'→ canonical alias of',prior[0],flush=True);continue
            if metadata.get('private') or metadata.get('disabled'):
                record.update(status='excluded',reason='Repository is private or disabled')
            elif metadata['stargazers_count']<10:
                record.update(status='excluded',reason='Fewer than 10 GitHub stars at collection time')
            else:
                readme_url='https://api.github.com/repos/'+metadata['full_name']+'/readme'
                readme=fetch_public(readme_url,accept='application/vnd.github.raw+json',offline=not args.online)
                body=readme['body'].decode(errors='replace')
                if len(body.strip())<50:
                    record.update(status='needs-review',reason='README is too short for a useful description')
                else:
                    record.update(readmeUrl=readme_url,readmeCheckedAt=readme['checkedAt'],readmeCharacters=len(body),readmeCacheUrl=readme_url,readmeExcerpt=body[:600])
                    # License facts remain available for editorial display, but are not an admission gate.
                    record.update(status='verified',reason=None)
            processed+=1
            print(repo,'→',record['status'],record['stars'],'stars', (metadata.get('license') or {}).get('spdx_id'),flush=True)
        except Deferred as error:
            record.update(status='pending',reason=str(error));_write(evidence_path,evidence);print('Deferred:',error,flush=True);break
        except RuntimeError as error:
            if str(error).startswith('Anonymous request failed'):
                record.update(status='pending',reason=str(error));_write(evidence_path,evidence)
                print('Deferred network request; progress preserved:',error,flush=True);break
            record.update(status='needs-review',reason=str(error));processed+=1;print(repo,str(error),flush=True)
        except (KeyError,json.JSONDecodeError) as error:
            record.update(status='needs-review',reason=str(error));processed+=1;print(repo,str(error),flush=True)
        _write(evidence_path,evidence)
    print('Progress:',{status:sum(e.get('status')==status for e in evidence.values()) for status in ['verified','pending','needs-review','excluded']},flush=True)

if __name__=='__main__':main()
