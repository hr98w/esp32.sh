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

if __name__=='__main__':unittest.main()
