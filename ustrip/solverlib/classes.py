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

class SimGeometry:
    def __init__(self):
        self.csx    = None
        self.ports  = None
        self.simbox = None

class Port:
    def __init__(self) -> None:
        self.geo = None
        self.num = None
        self.dir = None

class MSLPort(Port):
    def __init_(self, geo, num, dir) -> None:
        self.geo = geo
        self.num = num
        self.dir = dir

class RWGPort(Port):
    def __init_(self, geo, num, dir) -> None:
        self.geo = geo
        self.num = num
        self.dir = dir


class MicroStrip(SimGeometry):
    def __init__(self) -> None:
        self.ustrip    = None
        self.substrate = None

    class uStrip:
        def __init__(self, geo, mat) -> None:
            self.geo = geo
            self.mat = mat

    class Substrate:
        def __init__(self, geo, mat) -> None:
            self.geo = geo
            self.mat = mat
