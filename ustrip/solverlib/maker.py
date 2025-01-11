import os, sys, tempfile

class CSXMaker:
    def __init__(self) -> None:
        self.simgeo = None
        self.csx    = None
    def add_stl(self, arg):
        raise NotImplementedError
    def make_csx(self):
        raise NotImplementedError
    def run_appcsxcad(self):
        with tempfile.TemporaryDirectory() as tmp:
            model_path = os.path.join(tmp, 'model.xml')
            self.csx.Write2XML(model_path)
            os.system('AppCSXCAD "{}"'.format(model_path))
            sys.exit(0)



