import unittest
import logging
import src.puller as puller

class QueryTest(unittest.TestCase):
  def setUp(self):
    logging.basicConfig(filename='./helper_test.log', level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    self.logger = logging.getLogger(__name__)

    # generating class
    self.caller = puller.HNCaller('test/static/conf.json', self.logger)
    self.caller.construct_call()

  def test_setup(self):
    self.assertEqual(self.caller.terms, ['haskell', 'node.js', 'ocaml'])
    self.assertEqual(self.caller.tags, ['story', 'front_page'])

  def test_construct_call(self):
    expected_return = 'http://hn.algolia.com/api/v1/search?query=(haskell,node.js,ocaml)&tags=(story,front_page)'
    self.assertEqual(self.caller.construct_call(), expected_return)

  def test_process_call(self):
    url_call = self.caller.construct_call()
    api_return = self.caller.process_call(url_call)
    self.assertTrue(len(api_return) > 0)

if __name__ == '__main__':
  unittest.main()
