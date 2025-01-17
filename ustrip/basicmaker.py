import tempfile, logging
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
        fnargs = self._aext.get_filename_args(istl.filename)
        self.logger.debug(f'STL filename args: {fnargs.keys()} {fnargs.values()}')

        dispatch = {
            USTRIP:    self._add_element,
            SUBSTRATE: self._add_element,
            }

        dispatch.get(self.np.parsed[ELEMENT])(istl, fnargs)

    def make_csx(self):
        for e in self.simgeo.elements:
            self.logger.debug(f'Make CSX element: {e}')
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
        self.logger.debug(f'BBox Start: {start} BBox Stop: {stop}')
        e = emsclass.GeoEle()
        e.load_dict(self._aext.get_filename_args(istl.filename))
        e.istl = istl
        self.simgeo.elements.append(e)

    def _draw_element(self, ele):
        #mat = self.csx.AddMetal(ele.name)
        #if ele.material in METALS else \
        mat = self.csx.AddMaterial(ele.name)
        mat.SetColor(ele.color)

        #if np.any(np.isclose(ele.bbox[1] - ele.bbox[0]), 0):
        #    mat.AddBox(ele.bbox[0], ele.bbox[1], priority=ele.priority)
        #    continue

        tfname = f'{self.temp.name}/{ele.name}_{ele.number}.stl'
        f = open(tfname, 'wb')
        ele.istl.stl_byio.seek(0)
        f.write(ele.istl.stl_byio.read())
        f.close()
        prim = mat.AddPolyhedronReader(tfname, priority=int(ele.priority))
        prim.ReadFile()
        self.logger.debug(f'PolyhedronReader got BBOX: {prim.GetBoundBox()}')








