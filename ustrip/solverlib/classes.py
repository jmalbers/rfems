# EMSolver 'Worker' Classes
from constants import *

class Importer:
    def __init__(self) -> None:
        self.imports = {}
    def import_geo(self, filename):
        raise NotImplementedError

class Mesher:
    def __init__(self) -> None:
        ...
    def mesh_csx(self, csx):
        raise NotImplementedError

# Simulation Geometry Classes

class SimGeometry:
    def __init__(self):
        self.csx      = None
        self.elements = []
        self.ports    = []
        self.simbox   = []
        self.dmpbox   = []

class GeoEle:
    def __init__(self, name, **kw) -> None:
            self.name = name
            self.geo  = kw['geo'] if 'geo' in kw.keys() else None
            self.mat  = kw['mat'] if 'mat' in kw.keys() else None
            self.num  = kw['num'] if 'num' in kw.keys() else None
            self.pri  = kw['pri'] if 'pri' in kw.keys() else None
            self.col  = kw['col'] if 'col' in kw.keys() else None
            self.bbox = None

class Port:
    def __init__(self, **kw) -> None:
        self.name = None
        self.geo  = None
        self.num  = None
        self.dir  = None
        self.zo   = None
        self.exc  = None

        if 'pdict' in kw.keys():
            self._load_dict(kw['pdict'])

    def _load_dict(self, param):
        self.name = param[ELEMENT] if ELEMENT in param.keys() else None
        self.num  = param[NUMBER] if NUMBER in param.keys() else None
        self.dir  = param[DIRECTION] if DIRECTION in param.keys() else None
        self.z0   = param[Z0] if Z0 in param.keys() else None
        self.exc  = param[EXCITE] if EXCITE in param.keys() else None


