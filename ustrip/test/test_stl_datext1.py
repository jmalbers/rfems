import sys
import unittest

sys.path.append("../")
from solverlib.stl import StlDataExtractor, StlImporter
from solverlib.constants import DIRECTIONS, STL_TOL
import numpy as np


FILE_PATH = 'test_files/'
STL_FILE  = 'imp_test1.stl'

BBOX_START       = np.array([-45., -1., 0.])
BBOX_STOP        = np.array([45., 1., 1.67])
BBOX_STOP_PLANAR = np.array([45., 1., STL_TOL])

RWG_BBOX_START   = np.array([-20., -5., 0.])
RWG_BBOX_STOP    = np.array([20., 5., 1.])
RWG_WIDTH        = 40.0
RWG_HEIGHT       = 10.0


class TestStlDataParserBasic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.imp = StlImporter()
        cls.uut = StlDataExtractor()
        cls.stl = cls.imp.import_stl(FILE_PATH + STL_FILE)
        cls.stl.stl_data = cls.imp._make_npdata(cls.stl.stl_byio)

    def test_get_bbox3d(self):
        _start, _stop = self.uut.get_bbox(self.stl.stl_data)
        self.assertTrue(np.all(np.equal(_start, BBOX_START)))
        self.assertTrue(np.all(np.equal(_stop, BBOX_STOP)))

    def test_get_bbox2d(self):
        ...
        # Make sure items w/ <= STL_TOL return 2d values

    def test_get_rwgport_dim(self):
        x, y = self.uut.get_rwgport_dim(DIRECTIONS['y'], RWG_BBOX_START, RWG_BBOX_STOP)
        self.assertEqual(x, RWG_WIDTH)
        self.assertEqual(y, RWG_HEIGHT)

if __name__ == "__main__":
    unittest.main()