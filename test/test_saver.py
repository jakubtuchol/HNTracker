import src.saver as saver
import unittest

class SaveTest(unittest.TestCase):
    def setUp(self):
        # setting up logging
        logging.basicConfig(filename='./saver_test.log', level=logging.DEBUG,
                            format='%(asctime)s %(message)s')
        self.logger = logging.getLogger(__name__)
        
    def test_save(self):
        pass

if __name__ == '__main__':
    unittest.main()
