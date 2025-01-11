import sys
import unittest
import zipfile

sys.path.append("../")
from solverlib.stl import StlImporter

FILE_PATH    = 'test_files/'
STL_FILE     = 'imp_test1.stl'
ZIP_FILE     = 'ziptest.zip'
ZIP_CONTENTS = ['substrate', 'port_1_msl', 'port_2_msl', 'ustrip_thru']

class TestStlImporterBasic(unittest.TestCase):

    def setUp(self):
        self.uut = StlImporter()

    def test_import_stl(self):
        imp = self.uut.import_stl(FILE_PATH + STL_FILE)
        self.assertEqual(imp.filename, STL_FILE.split('.')[0])

    def test_make_npdata(self):
        imp = self.uut.import_stl(FILE_PATH + STL_FILE)
        imp.stl_data = self.uut._make_npdata(imp.stl_byio)
        self.assertEqual(len(imp.stl_data), 12)

    def test_open_bad_zip(self):
        with self.assertRaises(zipfile.BadZipFile):
            self.uut._unzip_models(FILE_PATH + STL_FILE)

    def test_open_zip(self):
        self.uut._unzip_models(FILE_PATH + ZIP_FILE)
        self.uut.tmpdir.cleanup()

    def test_import_zip(self):
        self.uut.import_zip(FILE_PATH+ZIP_FILE)
        for i in self.uut.imports:
            self.assertTrue(i.filename in ZIP_CONTENTS)
            
if __name__ == "__main__":
    unittest.main()