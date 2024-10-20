from constants import *

# ------------------------------------------------------------------------------
# EMSolver 'Worker' Classes
# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------
# Simulation Geometry Classes
# ------------------------------------------------------------------------------

class SimGeometry:
    def __init__(self):
        self.csx      = None
        self.elements = []
        self.ports    = []
        self.simbox   = []
        self.dmpbox   = []

class GeoEle:
    def __init__(self, **kw) -> None:
            self.name = None
            self.num  = None
            self.mat  = None
            self.pri  = None
            self.kap  = None
            self.eps  = None

            self.col  = None
            self.geo  = None

            if 'init_dict' in kw.keys():
                 self._load_dict(kw['init_dict'])

    def _load_dict(self, param):
        self.name = param[ELEMENT]  if ELEMENT  in param.keys() else None
        self.num  = param[NUMBER]   if NUMBER   in param.keys() else None
        self.mat  = param[MATERIAL] if MATERIAL in param.keys() else None
        self.pri  = param[PRIORITY] if PRIORITY in param.keys() else None
        self.kap  = param[KAPPA]    if KAPPA    in param.keys() else None
        self.eps  = param[EPSILON]  if EPSILON  in param.keys() else None

class Port:
    def __init__(self, **kw) -> None:
        self.name = None
        self.num  = None
        self.dir  = None
        self.zo   = None
        self.exc  = None

        self.col  = None
        self.geo  = None

        if 'init_dict' in kw.keys():
            self._load_dict(kw['init_dict'])

    def _load_dict(self, param):
        self.name = param[ELEMENT]   if ELEMENT   in param.keys() else None
        self.num  = param[NUMBER]    if NUMBER    in param.keys() else None
        self.dir  = param[DIRECTION] if DIRECTION in param.keys() else None
        self.z0   = param[Z0]        if Z0        in param.keys() else None
        self.exc  = param[EXCITE]    if EXCITE    in param.keys() else None


