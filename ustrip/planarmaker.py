# To Do:
#   * Add cubic substrate import function
#   * Add strip import function
#   * Add port import function

import numpy as np
import os, tempfile, sys
from CSXCAD import ContinuousStructure
from solverlib.classes import MicroStrip
from solverlib.maker import Maker

SIMGEO_ELEMENTS = 'port', 'air'
USTRIP_ELEMENTS = 'ustrip', 'substrate'


class PlanarMaker(Maker):
    """Geometer is the thing what turns triangles into CSX"""
    def __init__(self, rfstruct=None) -> None:
        self.geo = MicroStrip()

    def add_stl(self, stl: np.array, name):
        ...

    def add_dxf(self, dxf, name):
        ...







