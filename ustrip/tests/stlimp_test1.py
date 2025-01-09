import sys
import os
import logging
import unittest

logger = logging.getLogger(__file__)
sys.path.append("../")
from solverlib.stl import StlImporter


FILENAME = 'imp_test1.stl'
STL_PATH = 'test_files/'

class TestStlImporter(unittest.TestCase):

    def setUp(self):
        self.imp = StlImporter()
        logger.info('Importer initialized!')

    def test_triangleCount(self):
        self.imp.parse_stl(STL_PATH + FILENAME)
        logger.info('STL parsed.')
        tri = len(self.imp.imports[os.path.splitext(FILENAME)[0]])
        self.assertEqual(tri, 12, f'Expected 12 trianges got {tri}')
        logger.info(f'SUCCESS: {tri} triangles parsed from {FILENAME}!')

    def test_notZip(self):
        with self.assertRaises(TypeError):
            self.imp.unzip_models(STL_PATH + FILENAME)

if __name__ == "__main__":
    unittest.main()