import os, sys, tempfile, logging

class CSXMaker:
    def __init__(self) -> None:
        self.simgeo = None
        self.csx    = None
        self.temp   = None
        self.logger = None
    def add_stl(self, arg):
        raise NotImplementedError
    def make_csx(self):
        raise NotImplementedError
    def run_appcsxcad(self):
        model_path = os.path.join(self.temp.name, 'model.xml')
        self.csx.Write2XML(model_path)
        os.system(f'AppCSXCAD {model_path}')



