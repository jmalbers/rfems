class Maker:
    def __init__(self) -> None:
        ...
    def add_geo(self):
        raise NotImplementedError
    
class Importer:
    def __init__(self) -> None:
        ...
    def import_file(self, filename):
        raise NotImplementedError
    
class Mesher:
    def __init__(self) -> None:
        ...
    def mesh_geo(self, geo):
        raise NotImplementedError