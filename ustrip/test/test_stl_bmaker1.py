import sys, unittest, logging

sys.path.append("../")
from basicmaker import BasicMaker
from solverlib.stl import StlImporter, StlArgsExtractor, StlDataExtractor
from solverlib.constants import *


FILE_PATH      = 'test_files/'
USTRIP_FILE    = 'ustrip n=1 pri=3 mat=copper.stl'
SUBSTRATE_FILE = 'substrate.stl'
PORT_FILE      = 'lumport n=2 dir=z exc=0.stl'

# Needs test for add_stl function

class TestBasicMakerBasic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.imp  = StlImporter()
        cls.aext = StlArgsExtractor()
        #logging.basicConfig(level=logging.DEBUG)

        cls.istl = cls.imp.import_stl(FILE_PATH + USTRIP_FILE)
        cls.istl.stl_data = cls.imp._make_npdata(cls.istl.stl_byio)

    @classmethod
    def tearDownClass(cls):
        ...

    def setUp(self):
        self.uut = BasicMaker()

    def tearDown(self):
        self.uut.tmp.cleanup()

    def test_add_element(self):
        self.uut._add_element(self.istl)

        self.assertEqual(self.uut.geo.elements[0].name,     'ustrip')
        self.assertEqual(self.uut.geo.elements[0].number,   '1')
        self.assertEqual(self.uut.geo.elements[0].material, 'copper')
        self.assertEqual(self.uut.geo.elements[0].priority, '3')

    def test_draw_element(self):
        self.uut._add_element(self.istl)

        self.assertTrue(len(self.uut.geo.elements) == 1)
        self.uut.geo.elements[0].color = COLORS[RED]
        self.uut._draw_element(self.uut.geo.elements[0])

        self.uut.tmp.cleanup()

    def test_add_port(self):
        istl = self.imp.import_stl(FILE_PATH + PORT_FILE)
        istl.stl_data = self.imp._make_npdata(istl.stl_byio)
        self.uut._add_port(istl)

        self.assertEqual(len(self.uut.geo.ports), 1)
        self.assertEqual(self.uut.geo.ports[0].name,      'lumport')
        self.assertEqual(self.uut.geo.ports[0].number,    '2')
        self.assertEqual(self.uut.geo.ports[0].direction, 'z')
        self.assertEqual(self.uut.geo.ports[0].excite,    '0')

    @unittest.skip
    def test_runapp_csxcad(self):
        istl = self.imp.import_stl(FILE_PATH + SUBSTRATE_FILE)
        istl.stl_data = self.imp._make_npdata(istl.stl_byio)

        self.uut._add_element(istl)
        self.uut.geo.elements[0].color = COLORS[SUBSTRATE]
        self.uut.geo.elements[0].priority = 1
        self.uut.geo.elements[0].number = 1

        self.uut._draw_element(self.uut.geo.elements[0])
        self.uut.run_appcsxcad()
        self.uut.tmp.cleanup()

if __name__ == "__main__":
    unittest.main()