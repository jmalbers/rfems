from solverlib.constants import *

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
        self.elements = []
        self.ports    = []
        self.simbox   = []
        self.mshbox   = []
        self.dmpbox   = []

class GeoEle:
    def __init__(self) -> None:
            self.name     = None
            self.number   = None
            self.material = None
            self.priority = None
            self.kappa    = None
            self.epsilon  = None
            self.color    = None
            
            self.istl = None
            self.bbox = None

    def load_dict(self, idict):
        self.name     = idict[ELEMENT]  if ELEMENT  in idict.keys() else None
        self.number   = idict[NUMBER]   if NUMBER   in idict.keys() else None
        self.material = idict[MATERIAL] if MATERIAL in idict.keys() else None
        self.priority = idict[PRIORITY] if PRIORITY in idict.keys() else None
        self.kappa    = idict[KAPPA]    if KAPPA    in idict.keys() else None
        self.epsilon  = idict[EPSILON]  if EPSILON  in idict.keys() else None
        self.color    = idict[COLOR]    if COLOR  in idict.keys() else None

class Port:
    def __init__(self, bbox=None, **kw) -> None:
        self.name      = None
        self.number    = None
        self.direction = None
        self.zo        = None
        self.excite    = None
        self.color = None
        
        self.bbox  = bbox
        self.geo   = None
        self.port  = None

        if 'init_dict' in kw.keys():
            self._load_dict(kw['init_dict'])

    def _load_dict(self, param):
        self.name      = param[ELEMENT]   if ELEMENT   in param.keys() else None
        self.number    = param[NUMBER]    if NUMBER    in param.keys() else None
        self.direction = param[DIRECTION] if DIRECTION in param.keys() else None
        self.z0        = param[Z0]        if Z0        in param.keys() else None
        self.excite    = param[EXCITE]    if EXCITE    in param.keys() else None


