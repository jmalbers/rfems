# To Do:
#   * Add cubic substrate import function
#   * Add strip import function
#   * Add port import function

import numpy as np
import os, tempfile, sys
from CSXCAD import ContinuousStructure
from solverlib.classes import SimGeometry, GeoEle, Port
from solverlib.constants import *
from solverlib.maker import Maker
from solverlib.stl import StlNameParser, StlDataParser

class PlanarMaker(Maker):
    def __init__(self) -> None:
        self.np  = StlNameParser()
        self.dp  = StlDataParser()
        self.geo = SimGeometry()

    def add_stl(self, stl: np.array, filename):
        if not self.np.parse_filename(filename):
            return False

        dispatch = {
            MSL_PORT:  self._add_port,
            RWG_PORT:  self._add_port,
            LUM_PORT:  self._add_port,
            USTRIP:    self._add_element,
            SUBSTRATE: self._add_element,
            DUMP_BOX:  self._add_element,
            }

        dispatch.get(self.np.parsed[ELEMENT])()

    def add_dxf(self, dxf, geoname):
        ...

    def _add_port(self):
        ...

    def _add_element(self):
        ...







