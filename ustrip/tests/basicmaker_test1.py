import sys
import unittest

sys.path.append("../")
from basicmaker import BasicMaker
from solverlib.stl import StlImporter, StlNameParser
from solverlib.constants import *


FILE_PATH = 'test_files/'
STL_FILE  = 'ustrip n=1 pri=3 mat=copper.stl'

class TestBasicMakerBasic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.imp = StlImporter()
        cls.par = StlNameParser()
        cls.imp.parse_stl(FILE_PATH + STL_FILE)
        cls.test_key = list(cls.imp.imports.keys())[0]
        cls.test_val = cls.imp.imports[cls.test_key]
        cls.par.parse_filename(cls.test_key)

    def setUp(self):
        self.uut = BasicMaker()

    def test_add_element(self):
        self.uut._add_element(self.test_val, self.par.parsed)
        self.assertEqual(self.uut.simgeo.elements[0].name, 'ustrip')
        self.assertEqual(self.uut.simgeo.elements[0].number, '1')
        self.assertEqual(self.uut.simgeo.elements[0].material, 'copper')
        self.assertEqual(self.uut.simgeo.elements[0].geo, self.test_val)

    def test_draw_element(self):
        print(self.test_val)
        self.uut._add_element(self.test_val, self.par.parsed)
        self.uut.simgeo.elements[0].color = COLORS[RED]
        self.uut._draw_element(self.uut.simgeo.elements[0])
        
if __name__ == "__main__":
    unittest.main()