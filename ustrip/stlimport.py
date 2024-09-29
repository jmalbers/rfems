import numpy as np
import zipfile, tempfile, os
from solverlib.classes import Importer

class StlImporter(Importer):
    """ STL Importer

        Imports STL geometries and materials data for use with EM Solver / openEMS


        """

    def __init__(self) -> None:
        self.imports     = {}
        self.tmpdir      : tempfile.TemporaryDirectory

    def import_file(self, filename):
        if filename.endswith('.zip'):
            self.unzip_models(filename)

        for r, _, f in os.walk(self.tmpdir.name):
            for name in f:
                self.parse_stl(os.path.join(r, name))
        self.tmpdir.cleanup()

    def parse_stl(self, filename):

        data  = []
        facet = []

        with open(filename, 'rb') as f:
            if f.read(5) != b'solid':
                raise ValueError(f"'{filename}' is unsupported STL format.")

            for ln in f:
                d = ln.split()
                if d[0] == b'endfacet' and facet:
                    data.append(np.array(facet))
                    facet = []
                if d[0] == b'vertex' and len(d) == 4:
                    facet.append([ float(x) for x in d[1:] ])

        self.imports.update({filename : data})

    def unzip_models(self, filename):
        if not zipfile.is_zipfile(filename):
            raise TypeError(f"{filename} is not zip file.")

        zip = zipfile.ZipFile(filename)
        self.tmpdir = tempfile.TemporaryDirectory()
        
        for info in zip.infolist():
            if info.is_dir():
                continue
            root, ext = os.path.splitext(info.filename)
            if ext == '.stl':
                zip.extract(info, path=str(self.tmpdir.name))