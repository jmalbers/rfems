import sys
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)
sys.path.append("../")
from solverlib.stl import StlImporter

FILENAME = 'ziptest.zip'
STL_PATH = 'test_files/'

logger.info('\nStarting STL Importer zip file test.\n')
imp = StlImporter()
logger.info('Importer initialized!\n')
imp.unzip_models(STL_PATH + FILENAME)
logger.info('File unzipped to temp directory.\n')
# Test of some kind here
# More test
imp.tmpdir.cleanup() #Exception? 