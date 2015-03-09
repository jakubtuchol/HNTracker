import unittest

class QueryTest(unittest.TestCase):
  def test_multiple_terms(self):
    terms = ['haskell', 'node']
    exp_return = 'http://hn.algolia.com/api/v1/search?query=(haskell,node)'
    self.assertEqual(construct_call(search_terms=terms), exp_return)
  def test_basic_search(self):
    exp_return = 'http://hn.algolia.com/api/v1/search?query=haskell'
    self.assertEqual(construct_call('haskell'), exp_return )

class APITest(unittest.TestCase):
  def test_basic_query(self):
    url = 'http://hn.algolia.com/api/v1/search?query=haskell'
    self.assertTrue(call_api(url) > 0)

if __name__ == '__main__':
  unittest.main()
