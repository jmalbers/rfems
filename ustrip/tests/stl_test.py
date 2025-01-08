import sys
import numpy as np
sys.path.append("../")
from solverlib.stl import *

FILENAME = 'ustrip_thru.stl'

print('Starting STL Importer test.\n')
importer = StlImporter()
print('Importer initialized!\n')
importer.parse_stl(FILENAME)
print(f'{len(importer.stl_data[0])} triangles parsed from {FILENAME}!')
# Make planar geo 
# Open in CSXcad