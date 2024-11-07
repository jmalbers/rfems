# To Do:
#   * Add cubic substrate import function
#   * Add strip import function
#   * Add port import function

import numpy as np
import os, tempfile, sys
from CSXCAD import ContinuousStructure
import solverlib.classes as emsclass
from solverlib.constants import *
from solverlib.maker import Maker
from solverlib.stl import StlNameParser, StlDataParser

class PlanarMaker(Maker):
    def __init__(self) -> None:
        self.namep  = StlNameParser()
        self.datap  = StlDataParser()
        self.simgeo = emsclass.SimGeometry()

    def add_stl(self, fdtd, filename, stl: np.array):
        if not self.namep.parse_filename(filename):
            return False

        dispatch = {
            RWG_PORT:  self._add_port,
            LUM_PORT:  self._add_port,
            USTRIP:    self._add_element,
            SUBSTRATE: self._add_element,
            DUMP_BOX:  self._add_box,
            }

        dispatch.get(self.np.parsed[ELEMENT])(fdtd, filename, stl)

    def _add_port(self, fdtd, filename, stl):
        start, stop = self.datap.get_bbox(stl)
        self.simgeo.ports.append(emsclass.Port(bbox=[start, stop],
                                            init_dict=self.namep.parsed))
        fdtd.AddRwgPort(1, PEC, start, stop, X, Z, excite=1, priority=10)

    def _add_element(self, fdtd, filename, stl):
        start, stop = self.datap.get_bbox(stl)
        # Check if box shaped primative or polyhedron
        # CSX add material / metal
        self.simgeo.elements.append(emsclass.GeoEle(bbox=[start, stop],
                                                 init_dict=self.namep.parsed))
        # Add element geometry to csx from data parser input

    def _add_box(self):
        ...









