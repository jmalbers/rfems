# EMSolver 'Worker' Classes

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
    def __init__(self, name, geo, num, dir, **kw) -> None:
        self.name = name
        self.geo  = geo
        self.num  = num
        self.dir  = dir
        self.exc  = kw['exc'] if 'exc' in kw.keys() else None



