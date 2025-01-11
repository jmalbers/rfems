import sys
import unittest
import warnings

sys.path.append("../")
from solverlib.stl import StlArgsExtractor

FILE_PATH = 'test_files/'
GOOD_NAME = ['ustrip', 'mat=silver', 'pri=1', 'n=2']
BAD_NAME  = ['horses', 'mat=gold', 'pri=1']
BAD_ARGS  = ['ustrip', 'mat=silver', 'beef=1', 'n=2']

GOOD_KEYS = ['element', 'mat', 'pri', 'n']
GOOD_VALS = ['ustrip', 'silver', '1', '2']

class TestStlNameParserBasic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.uut = StlArgsExtractor()

    def test_split_name(self):
        t = ' '.join(GOOD_NAME)
        fn = self.uut._split_name(t)
        self.assertEqual(len(GOOD_NAME), len(fn))

        t = '_'.join(GOOD_NAME)
        fn = self.uut._split_name(t)
        self.assertEqual(len(GOOD_NAME), len(fn))

    def test_return_args(self):
        r = self.uut._return_args(GOOD_NAME)
        for i in range(1, len(GOOD_NAME)-1):
            self.assertEqual(r[i-1], GOOD_NAME[i])

    def test_get_argval(self):
        a, v = self.uut._get_argval(GOOD_NAME[1])
        self.assertEqual(a, 'mat')
        self.assertEqual(v, 'silver')

    def test_parse_badname(self):
        with self.assertRaises(TypeError):
            r = self.uut.get_filename_args(' '.join(BAD_NAME))
    
    def test_parse_goodname(self):
        r = self.uut.get_filename_args(' '.join(GOOD_NAME))
        for k in GOOD_KEYS:
            self.assertTrue(k in r.keys())
        for v in GOOD_VALS:
            self.assertTrue(v in r.values())

    def test_bad_args(self):
        r = self.uut.get_filename_args(' '.join(BAD_ARGS))
        self.assertFalse('beef' in r.keys())
        self.assertTrue('n' in r.keys())

if __name__ == "__main__":
    unittest.main()