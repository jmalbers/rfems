from CSXCAD import ContinuousStructure

class GeoMaker:
    """Geometer is the thing what turns triangles into CSX"""
    def __init__(self) -> None:
        pass

class SimGeometry:
    def __init__(self):
        self.csx = ContinuousStructure()
        self.mesh = None
        self.ports = []

class MicroStrip(SimGeometry):
    def __init__(self) -> None:
        self.sub_perm = None
        self.sub_xyz  = None
        self.cond_mat = None