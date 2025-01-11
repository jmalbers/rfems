import numpy as np
from CSXCAD import ContinuousStructure
import solverlib.classes as emsclass
from solverlib.constants import *
from solverlib.maker     import CSXMaker
from solverlib.stl       import StlArgsExtractor, StlDataExtractor, ImportedStl

class BasicMaker(CSXMaker):
    def __init__(self) -> None:
        self.simgeo = emsclass.SimGeometry()
        self.csx    = ContinuousStructure()
        
        self._aext  = StlArgsExtractor()
        self._dext  = StlDataExtractor()

    def add_stl(self, istl: ImportedStl):
        fnargs = self._aext.get_filename_args(istl.filename)

        dispatch = {
            USTRIP:    self._add_element,
            SUBSTRATE: self._add_element,
            }

        dispatch.get(self.np.parsed[ELEMENT])(istl, fnargs)

    def make_csx(self):
        for e in self.simgeo.elements:
            self._draw_element(e)

    #def _add_rwgport(self, fdtd, filename, stl):
    #    # refactor to resemble _add_element
    #    start, stop = self._dext.get_rwgport_bbox(stl)
    #    p = emsclass.Port(bbox=[start, stop],
    #                      init_dict=self._aext.parsed)
    #    p_w, p_h = self._dext.get_rwgport_dim(p.direction, start, stop)
    #    p.port = fdtd.AddRectWaveGuidePort(p.num, start, stop, p.direction,
    #                                      p_w, p_h, TE10, p.exc)
    #    self.simgeo.ports.append(p)

    def _add_element(self, istl: ImportedStl):
        start, stop = self._dext.get_bbox(istl.stl_data)
        e = emsclass.GeoEle()
        e.load_dict(self._aext.get_filename_args(istl.filename))
        e.istl = istl
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









