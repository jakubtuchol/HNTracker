import unittest
import logging
import os
import src.saver as saver
from src.helper import load_json

class SaveTest(unittest.TestCase):
  def setUp(self):
    # setting up logging
    logging.basicConfig(filename='./saver_test.log', level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    self.logger = logging.getLogger(__name__)

    self.saver = saver.HNSaver('src/static/save_conf.json', self.logger)
    self.csv_tester = 'src/static/test_csv.csv'
    
  def test_save_csv(self):
    json_file = load_json('src/static/save_test.json', self.logger)
    self.saver.save_csv(json_file['stories'])
    self.assertTrue(self.compare_files(self.saver.savefile, self.csv_tester))

  def test_save_copy(self):
    json_file = load_json('src/static/save_test.json', self.logger)          
    self.saver.save_csv(json_file['stories'])
    self.saver.save_csv(json_file['stories'])
    self.assertTrue(self.compare_files(self.saver.savefile, self.csv_tester))
    
  def tearDown(self):
    # removing previously created savefile
    if os.path.isfile(self.saver.savefile):
      os.remove(self.saver.savefile)
    if os.path.isfile(self.saver.idfile):
      os.remove(self.saver.idfile)

  # helper method for comparing two files
  def compare_files(self, filepath1, filepath2):
    file1 = open(filepath1, 'r')
    file2 = open(filepath2, 'r')
    f1 = file1.read().splitlines()
    f2 = file2.read().splitlines()
    if len(f1) != len(f2):
      return False
    for ix in range(len(f1)):
      if f1[ix] != f2[ix]:
        return False
    file1.close()
    file2.close()
    return True

if __name__ == '__main__':
  unittest.main()
