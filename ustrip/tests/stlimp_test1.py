import sys
import os
import logging

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)
sys.path.append("../")
from solverlib.stl import StlImporter


FILENAME = 'imp_test1.stl'
STL_PATH = 'test_files/'

logger.info('Starting STL Importer stl file read test.')
imp = StlImporter()
logger.info('Importer initialized!')
imp.parse_stl(STL_PATH + FILENAME)
logger.info('STL parsed.')
tri = len(imp.imports[os.path.splitext(FILENAME)[0]])
assert tri == 12, "XXXX STL Importer Test 1 FAIL: Expected 12 triangles."
logger.info(f'SUCCESS: {tri} triangles parsed from {FILENAME}!')
print("**** STL Importer Test 1: PASSED")