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
        self.csx     = ContinuousStructure()

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
        for e in self.simgeo.elements:
            self._draw_element(e)

    def _add_rwgport(self, fdtd, filename, stl):
        # refactor to resemble _add_element
        start, stop = self._datap.get_rwgport_bbox(stl)
        p = emsclass.Port(bbox=[start, stop],
                          init_dict=self._namep.parsed)
        p_w, p_h = self._datap.get_rwgport_dim(p.direction, start, stop)
        p.port = fdtd.AddRectWaveGuidePort(p.num, start, stop, p.direction,
                                          p_w, p_h, TE10, p.exc)
        self.simgeo.ports.append(p)

    def _add_element(self, stl, init_dict):
        start, stop = self._datap.get_bbox(stl)
        e = emsclass.GeoEle()
        e.load_dict(init_dict)
        e.geo = stl
        self.simgeo.elements.append(e)

    def _draw_element(self, ele):

        mat = self.csx.AddMetal(ele.material) if ele.material in METALS else \
              self.csx.AddMaterial(ele.material)
        mat.SetColor(ele.color)

        #if np.any(np.isclose(ele.bbox[1] - ele.bbox[0]), 0):
        #    mat.AddBox(x.bbox[0], x.bbox[1], priority=x.pri)
        #    continue

        ## Polyhedron reader needs an actual file to read not np array
        ## Need to add bytes.io attribute to retain ability to read with polyreader
        ## Importer needs class or? 
        prim = mat.AddPolyhedronReader(ele.geo[0], priority=int(ele.priority))
        prim.ReadFile()









