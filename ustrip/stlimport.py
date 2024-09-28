import numpy as np
import zipfile, tempfile, os, sys, argparse, platform, struct
from solverlib.classes import Importer

class StlImporter(Importer):
    """ STL Importer

        Imports STL geometries and materials data for use with EM Solver / openEMS


        """

    def __init__(self, geofunc: function) -> None:
        self.stl_data  = []
        self.to_geomaker = geofunc

    def import_file(self, filename):
        ...

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

        self.stl_data.append(data)

"""
    def unzip_models(self, filename, dirname):
        root, ext = os.path.splitext(filename)
        if ext != '.zip':
            filename = f'{root}.zip'
        zf = zipfile.ZipFile(filename)
        data = {}
        for info in zf.infolist():
            if not info.is_dir():
                root, ext = os.path.splitext(info.filename)
                if ext == '.stl':
                    name = os.path.basename(root)
                    path = zf.extract(info, dirname)
                    data[name] = path
                else:
                    print(f'WARNING: ignoring {info.filename}, only .stl files allowed')
        return data"""