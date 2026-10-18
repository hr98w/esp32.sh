import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import verify_projects

class ProjectTransportTests(unittest.TestCase):
 def test_network_failure_keeps_pending_and_stops_before_next_repository(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);data=root/'data/collection';data.mkdir(parents=True)
   (data/'project-candidates.json').write_text(json.dumps({'example/a':{'repository':'example/a'},'example/b':{'repository':'example/b'}}))
   with patch.object(verify_projects,'ROOT',root),patch.object(verify_projects,'fetch_public',side_effect=RuntimeError('Anonymous request failed (6): DNS unavailable')) as request,patch('sys.argv',['verify_projects.py','--online']),contextlib.redirect_stdout(io.StringIO()):
    verify_projects.main()
   evidence=json.loads((data/'repository-evidence.json').read_text())
   self.assertEqual(request.call_count,1)
   self.assertEqual(evidence['example/a']['status'],'pending')
   self.assertNotIn('example/b',evidence)


class ProjectLicensePolicyTests(unittest.TestCase):
 def test_missing_or_nonstandard_license_does_not_block_public_source_intake(self):
  for license_info in [None, {'spdx_id':'NOASSERTION'}, {'spdx_id':'LicenseRef-NonCommercial'}]:
   with self.subTest(license=license_info),tempfile.TemporaryDirectory() as directory:
    root=Path(directory);data=root/'data/collection';data.mkdir(parents=True)
    (data/'project-candidates.json').write_text(json.dumps({'example/a':{'repository':'example/a'}}))
    metadata={'full_name':'example/a','id':123,'stargazers_count':20,'default_branch':'main','license':license_info,'private':False,'disabled':False}
    responses=[{'body':json.dumps(metadata).encode(),'checkedAt':'2026-10-18T00:00:00Z','url':'https://api.github.com/repos/example/a'}, {'body':b'# ESP32 project\n'+b'Useful source and documentation. '*4,'checkedAt':'2026-10-18T00:00:01Z'}]
    with patch.object(verify_projects,'ROOT',root),patch.object(verify_projects,'fetch_public',side_effect=responses),patch('sys.argv',['verify_projects.py']),contextlib.redirect_stdout(io.StringIO()):
     verify_projects.main()
    evidence=json.loads((data/'repository-evidence.json').read_text())['example/a']
    self.assertEqual(evidence['status'],'verified')
    self.assertEqual(evidence['license'],license_info)
    self.assertIsNone(evidence['reason'])



class ProjectStarPolicyTests(unittest.TestCase):
 def test_owner_exception_retains_zero_star_projects_without_waiving_readme_check(self):
  for exempt,readme_length,status,calls in [(False,100,'excluded',1),(True,100,'verified',2),(True,0,'needs-review',2)]:
   with self.subTest(exempt=exempt,readme_length=readme_length),tempfile.TemporaryDirectory() as directory:
    root=Path(directory);data=root/'data/collection';data.mkdir(parents=True)
    (data/'project-candidates.json').write_text(json.dumps({'example/a':{'repository':'example/a'}}))
    if exempt:
     (root/'data/project-intake-overrides.json').write_text(json.dumps({'example/a':{'starThresholdExempt':True,'approvedBy':'site-owner','approvedAt':'2026-10-18T00:00:00Z','reason':'Explicit owner request'}}))
    metadata={'full_name':'example/a','id':123,'stargazers_count':0,'default_branch':'main','private':False,'disabled':False}
    responses=[{'body':json.dumps(metadata).encode(),'checkedAt':'2026-10-18T00:00:00Z','url':'https://api.github.com/repos/example/a'}, {'body':b'x'*readme_length,'checkedAt':'2026-10-18T00:00:01Z'}]
    with patch.object(verify_projects,'ROOT',root),patch.object(verify_projects,'fetch_public',side_effect=responses) as request,patch('sys.argv',['verify_projects.py']),contextlib.redirect_stdout(io.StringIO()):
     verify_projects.main()
    record=json.loads((data/'repository-evidence.json').read_text())['example/a']
    self.assertEqual(record['status'],status)
    self.assertEqual(record['stars'],0)
    self.assertEqual(request.call_count,calls)

if __name__=='__main__':unittest.main()
