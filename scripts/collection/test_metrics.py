import contextlib,io,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import sync_metrics
from public_fetch import Deferred

class MetricsTests(unittest.TestCase):
 def fixture(self,temp):
  root=Path(temp);(root/'content/projects').mkdir(parents=True);(root/'data').mkdir()
  (root/'content/projects/alpha.md').write_text('---\nid: alpha\nname: Alpha\nrepository: https://github.com/example/alpha\n---\n')
  snapshot={'repository':'https://github.com/example/alpha','githubId':42,'stars':123,'checkedAt':'2026-10-15T17:00:00+00:00','pushedAt':None,'archived':False,'sourceUrl':'https://api.github.com/repos/example/alpha'}
  path=root/'data/repository-metrics.json';path.write_text(json.dumps({'alpha':snapshot}))
  return root,path,snapshot
 def run_main(self,root,result=None,error=None,args=None):
  with patch('sync_metrics.ROOT',root),patch('sys.argv',['sync_metrics.py']+(args or [])),patch('sync_metrics.fetch_public',return_value=result,side_effect=error),contextlib.redirect_stdout(io.StringIO()):sync_metrics.main()
 def response(self,id=42,stars=0,name='example/alpha'):
  return {'body':json.dumps({'full_name':name,'id':id,'stargazers_count':stars,'pushed_at':None,'archived':False}).encode(),'url':'https://api.github.com/repos/'+name,'checkedAt':'2026-10-15T19:00:00+00:00'}
 def test_failed_update_preserves_count_and_success_timestamp(self):
  with tempfile.TemporaryDirectory() as temp:
   root,path,before=self.fixture(temp)
   self.run_main(root,error=RuntimeError('HTTP 502'),args=['--online','--refresh'])
   self.assertEqual(json.loads(path.read_text())['alpha'],before)
 def test_recreated_or_renamed_repository_does_not_silently_replace_identity(self):
  for result in [self.response(id=99,stars=9999),self.response(name='different/repository')]:
   with self.subTest(result=result),tempfile.TemporaryDirectory() as temp:
    root,path,before=self.fixture(temp);self.run_main(root,result=result,args=['--online'])
    self.assertEqual(json.loads(path.read_text())['alpha'],before)
 def test_confirmed_zero_is_saved_as_a_real_measurement(self):
  with tempfile.TemporaryDirectory() as temp:
   root,path,_=self.fixture(temp);self.run_main(root,result=self.response(),args=['--online'])
   after=json.loads(path.read_text())['alpha'];self.assertEqual(after['stars'],0);self.assertEqual(after['checkedAt'],'2026-10-15T19:00:00+00:00')
 def test_offline_cache_miss_does_not_prevent_later_cached_records(self):
  with tempfile.TemporaryDirectory() as temp:
   root,path,before=self.fixture(temp)
   (root/'content/projects/beta.md').write_text('---\nid: beta\nname: Beta\nrepository: https://github.com/example/beta\n---\n')
   self.run_main(root,error=[Deferred('Offline cache miss'),self.response(id=43,stars=20,name='example/beta')])
   after=json.loads(path.read_text());self.assertEqual(after['alpha'],before);self.assertEqual(after['beta']['stars'],20)
if __name__=='__main__':unittest.main()
