import unittest
import logging
import src.helper as helper

class HelperTest(unittest.TestCase):
  def setUp(self):
    # setting up logging
    logging.basicConfig(filename='./helper_test.log', level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    self.logger = logging.getLogger(__name__)

    # json test files
    self.good_json = 'test/static/good_json.json'
    self.bad_json = 'test/static/bad_json.json'
    self.good_url = 'http://hn.algolia.com/api/v1/items/1'
    self.call_404 = 'http://hn.algolia.com/api/v1/items/:id'
    self.bad_url = 'http://algolia.com/v1/items/1'

  def test_jsonload_good(self):
    json_resp = helper.load_json(self.good_json, self.logger)
    self.assertIn('title', json_resp['glossary'])
    self.assertEqual(json_resp['glossary']['title'], 'example glossary')

  def test_jsonload_bad(self):
    self.assertRaises(ValueError, helper.load_json, self.bad_json, self.logger)
    # add in further test fixtures to test correct logging
    
  def test_apicall_good(self):
    json_resp = helper.call_api(self.good_url, self.logger)
    self.assertIn('id', json_resp)
    self.assertIn('created_at', json_resp)

  def test_404_call(self):
    json_resp = helper.call_api(self.call_404, self.logger)
    self.assertIs(json_resp, None)

  def test_apicall_bad(self):
    json_resp = helper.call_api(self.bad_url, self.logger)
    self.assertIs(json_resp, None)

if __name__ == '__main__':
  unittest.main()
