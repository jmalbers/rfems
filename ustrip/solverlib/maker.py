import os, sys, tempfile

class CSXMaker:
    def __init__(self) -> None:
        self.simgeo = None
        self._namep = None
        self._datap = None
    def add_stl(self, fdtd, filename, stl):
        raise NotImplementedError
    def make_csx(self):
        raise NotImplementedError
    def run_appcsxcad(self):
        with tempfile.TemporaryDirectory() as tmp:
            model_path = os.path.join(tmp.name, 'model.xml')
            self.simgeo.csx.Write2XML(model_path)
            os.system('AppCSXCAD "{}"'.format(model_path))
            sys.exit(0)


