import sys
import unittest

sys.path.append("../")
from solverlib.stl import StlDataParser

FILE_PATH = 'test_files/'
GOOD_NAME = ['ustrip', 'mat', 'pri', 'num', '']
BAD_NAME  = 'bad'

class TestStlDataParserBasic(unittest.TestCase):

    def setUp(self):
        self.uut = StlDataParser()

    def test_get_bbox(self):
        ...

    def test_get_rwgport_bbox(self):
        ...

    def test_get_rwgport_dim(self):
        ...
        
if __name__ == "__main__":
    unittest.main()