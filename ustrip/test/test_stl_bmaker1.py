import sys
import unittest

sys.path.append("../")
from basicmaker import BasicMaker
from solverlib.stl import StlImporter, StlArgsExtractor, StlDataExtractor
from solverlib.constants import *


FILE_PATH = 'test_files/'
STL_FILE  = 'ustrip n=1 pri=3 mat=copper.stl'
STL_FILE2 = 'substrate.stl'

class TestBasicMakerBasic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.imp  = StlImporter()
        cls.aext = StlArgsExtractor()

        cls.istl = cls.imp.import_stl(FILE_PATH + STL_FILE)
        cls.istl.stl_data = cls.imp._make_npdata(cls.istl.stl_byio)

    def setUp(self):
        self.uut = BasicMaker()

    def test_add_element(self):
        self.uut._add_element(self.istl)
        self.assertEqual(self.uut.simgeo.elements[0].name, 'ustrip')
        self.assertEqual(self.uut.simgeo.elements[0].number, '1')
        self.assertEqual(self.uut.simgeo.elements[0].material, 'copper')
        self.assertEqual(self.uut.simgeo.elements[0].priority, '3')

    def test_draw_element(self):
        self.uut._add_element(self.istl)
        self.uut.simgeo.elements[0].color = COLORS[RED]
        self.uut._draw_element(self.uut.simgeo.elements[0])

    #@unittest.skip
    def test_runapp_csxcad(self):
        import logging
        logging.basicConfig(level=logging.DEBUG)
        istl = self.imp.import_stl(FILE_PATH + STL_FILE2)
        istl.stl_data = self.imp._make_npdata(istl.stl_byio)

        self.uut._add_element(istl)
        self.uut.simgeo.elements[0].color = COLORS[RED]
        self.uut.simgeo.elements[0].priority = 1
        self.uut.simgeo.elements[0].number = 1

        self.uut._draw_element(self.uut.simgeo.elements[0])
        self.uut.run_appcsxcad()

if __name__ == "__main__":
    unittest.main()