import numpy as np
import zipfile, tempfile, os
from io import BytesIO
import warnings
from solverlib.classes import Importer
from solverlib.constants import *

class ImportedStl:
    def __init__(self):
        self.filename = ''
        self.stl_byio = None
        self.stl_data = None

class StlImporter(Importer):
    """ STL Importer

        Imports STL geometries and materials data for use with EM Solver / openEMS


        """
    def __init__(self) -> None:
        self.imports = []
        self.tmpdir  : tempfile.TemporaryDirectory

    def import_zip(self, filename):
        self._unzip_models(filename)
            
        for r, _, f in os.walk(self.tmpdir.name):
            for name in f:
                imp = self.import_stl(os.path.join(r, name))
                imp.stl_data = self._make_npdata(imp.stl_byio)
                self.imports.append(imp)

        self.tmpdir.cleanup()

    def import_stl(self, filename):
        imp = ImportedStl()
        imp.filename = os.path.splitext(os.path.split(filename)[1])[0]

        with open(filename, 'rb') as f:
            if f.read(5) != b'solid':
                raise ValueError(f"'{filename}' is unsupported STL format.")
            
            imp.stl_byio = BytesIO(f.read())
        
        return imp

    def _make_npdata(self, stl_byio: BytesIO):
        data  = []
        facet = []

        with stl_byio as f:
            for ln in f:
                d = ln.split()
                if d[0] == b'endfacet' and facet:
                    data.append(np.array(facet))
                    facet = []
                if d[0] == b'vertex' and len(d) == 4:
                    facet.append([ float(x) for x in d[1:]])

        return data

    def _unzip_models(self, filename):
        zip = zipfile.ZipFile(filename)
        self.tmpdir = tempfile.TemporaryDirectory()

        for info in zip.infolist():
            if info.is_dir():
                continue
            root, ext = os.path.splitext(info.filename)
            if ext == '.stl':
                zip.extract(info, path=str(self.tmpdir.name))

class StlDataExtractor:
    """ STL Data Parser

        Parses STL geometric data for bounding boxes, facet normal, etc


        """
    def __init__(self) -> None:
        ...

    def get_bbox(self, stl_data):
        start, stop = 0,0

        for facet in stl_data:
            for vertex in facet:
                start = vertex if start is None else np.minimum(vertex, start)
                stop  = vertex if stop is None else np.maximum(vertex, stop)

        idx = np.logical_or(stop - start < STL_TOL, np.isclose(stop - start, STL_TOL))
        start[idx] = stop[idx] = ((start + stop) / 2)[idx]
        return start, stop

    def get_rwgport_bbox(self, stl_data):
        return self.get_bbox

    def get_rwgport_dim(self, pdir, start, stop):
        # Possible error: bbox indices may not line up with DIRECTIONS constant
        dirs = list(DIRECTIONS.values())
        dirs.remove(pdir)
        dims = [abs(start[i]) + abs(stop[i]) for i in range(0, 2)]
        return max(dims), min(dims)


class StlArgsExtractor:
    """ STL Filename Parser

        Parses STL filename to retrieve modeling and simulation parameters.


        This really needs to just parse strings and return values rather than 
        store stuff.

        """
    def __init__(self) -> None:
        ...

    def get_filename_args(self, filename):
        fn = self._split_name(filename)
        if fn[0] not in VALID_ELEMENTS:
            raise TypeError(f"'{fn}' is invalid sim element.")
        
        parsed = {}
        parsed.update({ELEMENT: fn[0]})

        if parsed[ELEMENT] in PORT_TYPES:
            return parsed.update(self.get_port_args(parsed))

        for i in self._return_args(fn[1:]):
            a, v = self._get_argval(i)
            if a in FILENAME_ARGS:
                parsed.update({a: v})
            else: 
                warnings.warn(f"'{a}={v}' is invalid sim element argument.")

        return parsed

    def get_port_args(self, filename):
        ret = {}
        for i in self._return_args(filename):
            a, v = self._get_argval(i)
            if a in PORT_ARGS:
                ret.update({a: v})
            else: 
                warnings.warn(f"'{a}={v}' is invalid port argument.")

        return ret

    def _return_args(self, split_name):
        return list(filter(lambda x: ARG_SEPERATOR in x, split_name))

    def _get_argval(self, str_in):
        arg, _, value = str_in.partition(ARG_SEPERATOR)
        return arg, value

    def _split_name(self, filename) -> list:
        spl_char = '_' if '_' in filename else ' '
        return filename.split(spl_char)
