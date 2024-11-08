import numpy as np
import os, tempfile, sys
from CSXCAD import ContinuousStructure
import solverlib.classes as emsclass
from solverlib.constants import *
from solverlib.maker     import Maker
from solverlib.stl       import StlNameParser, StlDataParser

class PlanarMaker(Maker):
    def __init__(self) -> None:
        self.namep  = StlNameParser()
        self.datap  = StlDataParser()
        self.emsgeo = emsclass.SimGeometry()

    def add_stl(self, fdtd, filename, stl: np.array):
        if not self.namep.parse_filename(filename):
            return False

        dispatch = {
            RWG_PORT:  self._add_rwgport,
            LUM_PORT:  self._add_lumport,
            USTRIP:    self._add_element,
            SUBSTRATE: self._add_element,
            DUMP_BOX:  self._add_box,
            }

        dispatch.get(self.np.parsed[ELEMENT])(fdtd, filename, stl)

    def _add_rwgport(self, fdtd, filename, stl):
        start, stop = self.datap.get_rwgport_bbox(stl)
        p = emsclass.Port(bbox=[start, stop],
                          init_dict=self.namep.parsed)
        p_w, p_h = self.datap.get_rwgport_dim(p.dir, start, stop)
        #Port class needs a place to store return from AddRectWave...
        p.ems = fdtd.AddRectWaveGuidePort(p.num, start, stop, p.dir,
                                          p_w, p_h, TE10, p.exc)
        self.emsgeo.ports.append(p)

    def _add_lumport(self, fdtd, filename, stl):
       ...

    def _add_element(self, fdtd, filename, stl):
        start, stop = self.datap.get_bbox(stl)
        e = emsclass.GeoEle(bbox=[start, stop],
                                  init_dict=self.namep.parsed)
        # Check if box shaped primative or polyhedron
        # CSX add material / metal
        # Add element geometry to csx from data parser input
        self.emsgeo.elements.append(e)

    def _add_box(self):
        ...









