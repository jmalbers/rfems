import os, sys, tempfile

class CSXMaker:
    def __init__(self) -> None:
        self.simgeo = None
        self.csx    = None
        self.temp   = None

    def add_stl(self, arg):
        raise NotImplementedError
    def make_csx(self):
        raise NotImplementedError
    def run_appcsxcad(self):
        model_path = os.path.join(self.temp.name, 'model.xml')
        self.csx.Write2XML(model_path)
        with open(model_path, 'rb') as f:
            print(f.read())
            f.seek(0)
            os.system(f'AppCSXCAD {model_path}')



