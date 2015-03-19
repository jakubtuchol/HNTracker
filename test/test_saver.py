import unittest
import logging
import src.saver as saver

class SaveTest(unittest.TestCase):
  def setUp(self):
    # setting up logging
    logging.basicConfig(filename='./saver_test.log', level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    self.logger = logging.getLogger(__name__)

    self.saver = saver.HNSaver('./')
  def test_save_csv(self):
    

if __name__ == '__main__':
  unittest.main()
