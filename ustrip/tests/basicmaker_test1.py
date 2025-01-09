import sys
import unittest

sys.path.append("../")
from basicmaker import BasicMaker

FILE_PATH = 'test_files/'
GOOD_NAME = ['ustrip', 'mat', 'pri', 'num', '']
BAD_NAME  = 'bad'

class TestBasicMakerBasic(unittest.TestCase):

    def setUp(self):
        self.uut = BasicMaker()

    def test_add_element(self):
        ...

    def test_add_stl(self):
        ...

    def test_draw_elements(self):
        ...

    def test_parse_badname(self):
        ...
    
    def test_parse_goodname(self):
        ...

    def test_parse_port(self):
        ...
        
if __name__ == "__main__":
    unittest.main()