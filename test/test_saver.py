import unittest
import logging
import src.saver as saver
import src.helper as helper

class SaveTest(unittest.TestCase):
  def setUp(self):
    # setting up logging
    logging.basicConfig(filename='./saver_test.log', level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    self.logger = logging.getLogger(__name__)

    self.saver = saver.HNSaver('test/static/save_conf.json', self.logger)
    self.csv_tester = 'test/static/test_csv.csv'
    
  def test_save_csv(self):
    json_file = helper.load_json('test/static/save_test.json', self.logger)
    self.saver.save_csv(json_files['stories'])
    self.assertTrue(compare_files(self.saver.savefile, self.csv_tester))

  # helper method for comparing two files
  def compare_files(filepath1, filepath2):
    with open(filepath1, 'r').read().splitlines() as f1:
      with open(filepath2, 'r').read().splitlines() as f2:
        if len(f1) != len(f2):
          return False
        for ix in range(len(f1)):
          if f1[ix] != f2[ix]:
            return False

    return True

if __name__ == '__main__':
  unittest.main()
