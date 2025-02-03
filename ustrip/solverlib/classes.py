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
        self.elements   = []
        self.ports      = []
        self.mesh_boxes = []
        self.dump_box   = []

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

class Port:
    def __init__(self) -> None:
        self.name      = None
        self.number    = None
        self.direction = None
        self.zo        = None
        self.excite    = None
        self.color     = None

        self.istl      = None
        self.bbox      = None

    def load_dict(self, idict):
        self.name      = idict[ELEMENT]   if ELEMENT   in idict.keys() else None
        self.number    = idict[NUMBER]    if NUMBER    in idict.keys() else None
        self.direction = idict[DIRECTION] if DIRECTION in idict.keys() else None
        self.z0        = idict[Z0]        if Z0        in idict.keys() else None
        self.excite    = idict[EXCITE]    if EXCITE    in idict.keys() else None


