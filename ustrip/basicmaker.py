import numpy as np
from CSXCAD import ContinuousStructure
import solverlib.classes as emsclass
from solverlib.constants import *
from solverlib.maker     import CSXMaker
from solverlib.stl       import StlNameParser, StlDataParser

class BasicMaker(CSXMaker):
    def __init__(self) -> None:
        self._namep  = StlNameParser()
        self._datap  = StlDataParser()
        self.simgeo  = emsclass.SimGeometry()

    def add_stl(self, fdtd, filename, stl: np.array):
        if not self._namep.parse_filename(filename):
            return False

        dispatch = {
            RWG_PORT:  self._add_rwgport,
            USTRIP:    self._add_element,
            SUBSTRATE: self._add_element,
            }

        dispatch.get(self.np.parsed[ELEMENT])(fdtd, filename, stl)

    def make_csx(self):
        self.simgeo.csx = ContinuousStructure()
        self._draw_elements()

    def _add_rwgport(self, fdtd, filename, stl):
        start, stop = self._datap.get_rwgport_bbox(stl)
        p = emsclass.Port(bbox=[start, stop],
                          init_dict=self._namep.parsed)
        p_w, p_h = self._datap.get_rwgport_dim(p.dir, start, stop)
        p.ems = fdtd.AddRectWaveGuidePort(p.num, start, stop, p.dir,
                                          p_w, p_h, TE10, p.exc)
        self.simgeo.ports.append(p)

    def _add_element(self, fdtd, filename, stl):
        start, stop = self._datap.get_bbox(stl)
        e = emsclass.GeoEle(bbox=[start, stop],
                            init_dict=self._namep.parsed)
        self.simgeo.elements.append(e)

    def _draw_elements(self):

        for x in self.simgeo.elements:
            mat = self.simgeo.csx.AddMetal(x.mat) if x.mat in METALS else \
                  self.simgeo.csx.AddMaterial(x.mat)
            mat.SetColor(x.col)

            if np.any(np.isclose(x.bbox[1] - x.bbox[0]), 0):
                mat.AddBox(x.bbox[0], x.bbox[1], priority=x.pri)
                continue

            prim = mat.AddPolyhedronReader(x.name, priority=x.pri)
            prim.ReadFile()









