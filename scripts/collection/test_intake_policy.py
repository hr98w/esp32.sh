import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import report
from intake_policy import star_threshold_exempt

class StarExemptionReportTests(unittest.TestCase):
 def test_zero_star_owner_project_is_included_while_ordinary_project_stays_under_review(self):
  for approved, expected in [(False, 'needs-review'), (True, 'included')]:
   with self.subTest(approved=approved), tempfile.TemporaryDirectory() as directory:
    root=Path(directory);data=root/'data';collection=data/'collection';collection.mkdir(parents=True)
    (root/'docs/research').mkdir(parents=True)
    projects=root/'content/projects';projects.mkdir(parents=True)
    (projects/'example.md').write_text('---\n'+json.dumps({'id':'example','repository':'https://github.com/example/project'})+'\n---\n')
    (collection/'project-candidates.json').write_text(json.dumps({'example/project':{'repository':'example/project','sources':['https://github.com/example/project']}}))
    (collection/'repository-evidence.json').write_text(json.dumps({'example/project':{'repository':'example/project','status':'verified','stars':0}}))
    (data/'repository-metrics.json').write_text(json.dumps({'example':{'stars':0,'checkedAt':'2026-10-18T00:00:00Z'}}))
    if approved:
     (data/'project-intake-overrides.json').write_text(json.dumps({'example/project':{'starThresholdExempt':True,'approvedBy':'site-owner','approvedAt':'2026-10-18T00:00:00Z','reason':'Explicit owner request'}}))
     self.assertTrue(star_threshold_exempt(root,'https://github.com/Example/Project'))
     self.assertFalse(star_threshold_exempt(root,'example/different'))
    with patch.object(report,'ROOT',root), contextlib.redirect_stdout(io.StringIO()):report.main()
    queue=json.loads((collection/'queue.json').read_text())
    self.assertEqual(queue[0]['status'],expected)
    self.assertEqual(queue[0]['stars'],0)

if __name__=='__main__':unittest.main()
