import unittest
import logging
import helper

class HelperTest(unittest.TestCase):
  def setUp(self):
    # setting up logging
    logging.basicConfig(filename='./helper_test.log', level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    self.logger = logging.getLogger(__name__)

    # json test files
    self.good_json = './good_json.json'
    self.bad_json = './bad_json.json'
    self.good_url = ''
    self.bad_url = ''

  def tearDown(self):
    self.logger.close()

  def test_jsonload_good(self):
    json_resp = helper.load_json(self.good_json)
    self.assertIn('title', json_resp['glossary'])
    self.assertEqual(json_resp['glossary']['title'], 'example glossary')

  def test_jsonload_bad(self):
    self.assertRaises(ValueError, helper.load_json(self.bad_json, self.logger))
    # add in further test fixtures to test correct logging
    
  def test_apicall_good(self):
    pass

  def test_apicall_bad(self):
    pass

if __name__ == '__main__':
  unittest.main()
