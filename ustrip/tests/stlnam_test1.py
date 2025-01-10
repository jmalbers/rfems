import sys
import unittest

sys.path.append("../")
from solverlib.stl import StlNameParser

FILE_PATH = 'test_files/'
GOOD_NAME = ['ustrip', 'mat=silver', 'pri=1', 'n=2']
BAD_NAME  = ['horses', 'mat=gold', 'pri=1']
BAD_ARGS  = ['ustrip', 'mat=silver', 'beef=1', 'n=2']

class TestStlNameParserBasic(unittest.TestCase):

    def setUp(self):
        self.uut = StlNameParser()

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
        r = self.uut.parse_filename(' '.join(BAD_NAME))
        self.assertFalse(r)
        self.assertEqual(len(self.uut.parsed), 0)
    
    def test_parse_goodname(self):
        r = self.uut.parse_filename(' '.join(GOOD_NAME))
        self.assertTrue(r)
        self.assertEqual(len(self.uut.parsed), len(GOOD_NAME))

    def test_bad_args(self):
        r = self.uut.parse_filename(' '.join(BAD_ARGS))
        self.assertTrue(r)
        self.assertFalse('beef' in self.uut.parsed.keys())
        self.assertTrue('n' in self.uut.parsed.keys())

if __name__ == "__main__":
    unittest.main()