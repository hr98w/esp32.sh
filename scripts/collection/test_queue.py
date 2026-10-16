import unittest
from report import collapse_project_aliases
class QueueTests(unittest.TestCase):
 def test_renamed_repository_merges_sources_without_double_counting_public_records(self):
  entries=[dict(key='old/name',repository='New/Name',status='pending',sources=['https://directory.example.com/one']),dict(key='new/name',repository='new/name',status='included',content={'id':'stable-project-id'},sources=['https://directory.example.com/two'])]
  rows=collapse_project_aliases(entries)
  self.assertEqual(len(rows),1)
  self.assertEqual(rows[0]['status'],'included')
  self.assertEqual(rows[0]['content']['id'],'stable-project-id')
  self.assertEqual(len(rows[0]['sources']),2)
  self.assertEqual(rows[0]['discoveryKeys'],['old/name','new/name'])
if __name__=='__main__':unittest.main()
