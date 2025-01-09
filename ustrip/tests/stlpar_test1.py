import sys
import os
import unittest

sys.path.append("../")
from solverlib.stl import StlNameParser

FILE_PATH = 'test_files/'
GOOD_NAME = 'imp_test1.stl'
BAD_NAME  = 'bad'

class TestStlNameParserBasic(unittest.TestCase):

    def setUp(self):
        self.uut = StlNameParser()

    def test_parse_stl(self):
        self.uut.parse_stl(FILE_PATH + STL_FILE)
        tri = len(self.uut.imports[os.path.splitext(STL_FILE)[0]])
        self.assertEqual(tri, 12, f'Expected 12 trianges got {tri}')

    def test_open_bad_zip(self):
        with self.assertRaises(zipfile.BadZipFile):
            self.uut.unzip_models(FILE_PATH + STL_FILE)

    def test_open_zip(self):
        self.uut.unzip_models(FILE_PATH + ZIP_FILE)
        self.uut.tmpdir.cleanup()

    def test_import_geo_zip(self):
        self.uut.import_geo(FILE_PATH+ZIP_FILE)
        self.assertTrue(ZIP_CONTENTS in self.uut.imports.keys()) 

if __name__ == "__main__":
    unittest.main()