# To Do:
#   * Add cubic substrate import function
#   * Add strip import function
#   * Add port import function

import numpy as np
import os, tempfile, sys
from CSXCAD import ContinuousStructure
from solverlib.classes import Maker, SimGeometry

SIMGEO_ELEMENTS = 'port', 'air'
USTRIP_ELEMENTS = 'ustrip', 'substrate'


class PlanarMaker(Maker):
    """Geometer is the thing what turns triangles into CSX"""
    def __init__(self, rfstruct=None) -> None:
        self.geo      = MicroStrip()

    def add_stl(self, stl: np.array, name):
        ...

    def add_dxf(self, dxf, name):
        ...

    def run_appcsxcad(self):
        with tempfile.TemporaryDirectory() as tmp:
            model_path = os.path.join(tmp.name, 'model.xml')
            self.geo.csx.Write2XML(model_path)
            os.system('AppCSXCAD "{}"'.format(model_path))
            sys.exit(0)

def _get_bbox(data):
    start = None
    stop = None
    for facet in data:
        for v in facet:
            start = v if start is None else np.minimum(v, start)
            stop = v if stop is None else np.maximum(v, stop)
    return start, stop

def _is_rectocube(shape) -> bool:
    ...

def _get_normal(facet) -> np.float32:
    pass

def _bbox_corners(start, stop) -> np.array:
    ...

