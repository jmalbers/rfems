import tempfile, logging
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
        self.temp   = tempfile.TemporaryDirectory()

        self._aext  = StlArgsExtractor()
        self._dext  = StlDataExtractor()

        self.logger = logging.getLogger(self.__class__.__name__)

    def add_stl(self, istl: ImportedStl):
        self.logger.info(f"\n* Adding STL model {istl.filename} *")
        fnargs = self._aext.get_filename_args(istl.filename)
        self.logger.debug(f' STL filename args: {fnargs.keys()} {fnargs.values()}')

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
        self.logger.info(f'\n* Adding "{istl.filename}" to geometry *')

        e = emsclass.GeoEle()
        e.istl = istl
        e.load_dict(self._aext.get_filename_args(istl.filename))
        start, stop = self._dext.get_bbox(istl.stl_data)
        e.bbox = [start, stop]
        self.simgeo.elements.append(e)
        self.logger.debug(f'\n Data extractor output for "{e.name}" element '
                          f'\n Predicted bbox:\n {"-"*15}'
                          f'\n {start}\n {stop}')
    
    def _draw_element(self, ele):
        self.logger.info(f'\n* Drawing {ele.name} element in CSXCAD *')
        
        if ele.material in METALS:
            mat = self.csx.AddMetal(ele.name)
        else: 
            mat = self.csx.AddMaterial(ele.name)
        
        mat.SetColor(COLORS[ele.name])
        
        # ---------------------------------------------------------------------------- 

        # This logic ported over from original project is suspicious:
        # - This appears to trigger if an object is close enough to 2D
        # - What it doesn't consider is that the bbox only encloses the geometry
        # - I believe a 2D ustrip with 1/4 wave stub would just get turned into a box?
        # - Probably just remove it.

        #if np.any(np.isclose(ele.bbox[1] - ele.bbox[0], 0)):
        #    mat.AddBox(ele.bbox[0], ele.bbox[1], priority=ele.priority)
        #    self.logger.info(f'\n Drew box geometry for element "{ele.name}"')
        
        # ---------------------------------------------------------------------------- 

        tfname = f'{self.temp.name}/{ele.name}_{ele.number}.stl'
        self.logger.debug(f'\n Stashing in "{tfname}" for PolyhedronReader')

        with open(tfname, 'wb') as f:
            f.write(ele.istl.stl_byio.read())
            prim = mat.AddPolyhedronReader(tfname, priority=int(ele.priority))
            f.seek(0)
            prim.ReadFile()

        self.logger.debug(f'\n PolyhedronReader output for "{ele.name}" element '
                          f'\n Vertices: {prim.GetNumVertices()}\n Faces: {prim.GetNumFaces()}'
                          f'\n Actual bbox:\n {"-"*10}\n {np.array_str(prim.GetBoundBox(), precision=3, suppress_small=True)}')









