import os, sys, tempfile

class Maker:
    def __init__(self) -> None:
        self.geo    = None
        self.nparse = None
        self.gparse = None
    def add_stl(self, stl, name):
        raise NotImplementedError
    def add_dxf(self, dxf, name):
        raise NotImplementedError
    def run_appcsxcad(self):
        with tempfile.TemporaryDirectory() as tmp:
            model_path = os.path.join(tmp.name, 'model.xml')
            self.geo.csx.Write2XML(model_path)
            os.system('AppCSXCAD "{}"'.format(model_path))
            sys.exit(0)


