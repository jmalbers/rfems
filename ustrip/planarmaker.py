# To Do:
#   * Add cubic substrate import function
#   * Add strip import function
#   * Add port import function

import numpy as np
import os, tempfile, sys
from CSXCAD import ContinuousStructure
from solverlib.classes import MicroStrip
from solverlib.maker import Maker
from solverlib.stl import StlNameParser, StlDataParser

SIMGEO_ELEMENTS = 'port', 'air'
USTRIP_ELEMENTS = 'ustrip', 'substrate'


class PlanarMaker(Maker):
    """Geometer is the thing what turns triangles into CSX"""
    def __init__(self, rfstruct=None) -> None:
        self.np  = StlNameParser()
        self.dp  = StlDataParser()
        self.geo = MicroStrip()

    def add_stl(self, stl: np.array, filename):
        if not self.np.parse_filename(filename):
            return False
        

    def add_dxf(self, dxf, geoname):
        ...







