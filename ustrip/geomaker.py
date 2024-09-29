import numpy as np
from CSXCAD import ContinuousStructure
from solverlib.classes import Maker

SIMGEO_ELEMENTS = 'port', 'air'
USTRIP_ELEMENTS = 'ustrip', 'substrate'


class GeoMaker(Maker):
    """Geometer is the thing what turns triangles into CSX"""
    def __init__(self, rfstruct=None) -> None:
        self.rfstruct = rfstruct
        self.geo      = MicroStrip() 

    def add_geo(self, geo, name):
        if name.endswith(".stl"):
            self.add_stl(geo, name)
        else:
            raise TypeError(f"{name} not valid geometry type.")

    def add_stl(self, stl: np.array, name):
        ...

    def get_csx(self):
        return self.geo.csx


class SimGeometry:
    def __init__(self):
        self.csx = ContinuousStructure()
        self.mesh = None
        self.ports = []
        self.simbox = None

class MicroStrip(SimGeometry):
    def __init__(self) -> None:
        self.valid

    class uStrip:
        def __init__(self, geo, mat) -> None:
            self.geo = geo
            self.mat = mat
            self.csx = None

    class Substrate:
        def __init__(self, geo, mat) -> None:
            self.geo = geo
            self.mat = mat
            self.csx = None

            self.permitivity