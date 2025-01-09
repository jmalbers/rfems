import sys
import unittest

sys.path.append("../")
from solverlib.stl import StlNameParser

FILE_PATH = 'test_files/'
GOOD_NAME = ['ustrip', 'mat', 'pri', 'num', '']
BAD_NAME  = 'bad'

class TestStlNameParserBasic(unittest.TestCase):

    def setUp(self):
        self.uut = StlNameParser()

    def test_split_name(self):
        ...

    def test_return_args(self):
        ...

    def test_get_argval(self):
        ...

    def test_parse_badname(self):
        ...
    
    def test_parse_goodname(self):
        ...

    def test_parse_port(self):
        ...

if __name__ == "__main__":
    unittest.main()