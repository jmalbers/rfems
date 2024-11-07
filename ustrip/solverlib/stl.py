import numpy as np
import zipfile, tempfile, os
from solverlib.classes import Importer
from constants import *

class StlImporter(Importer):
    """ STL Importer

        Imports STL geometries and materials data for use with EM Solver / openEMS


        """

    def __init__(self) -> None:
        self.imports     = {}
        self.tmpdir      : tempfile.TemporaryDirectory

    def import_geo(self, filename):
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

class StlDataParser:
    def __init__(self) -> None:
        ...

    def get_bbox(self, stl_data):
        start, stop = None
        for facet in stl_data:
            for vertex in facet:
                start = vertex if start is None else np.minimum(vertex, start)
                stop  = vertex if stop is None else np.maximum(vertex, stop)

        idx = np.logical_or(stop - start < STL_TOL, np.isclose(stop - start, STL_TOL))
        start[idx] = stop[idx] = ((start + stop) / 2)[idx]
        return start, stop

class StlNameParser:
    def __init__(self) -> None:
        self.fn     = []
        self.parsed = {}

    def parse_filename(self, filename):
        self.fn = _split_name(filename)
        if self.fn[0] not in VALID_ELEMENTS:
            return False

        self.parsed = {}
        self.parsed.update({ELEMENT: self.fn[0]})

        if self.fn[0] in PORT_TYPES:
            return self.parse_port()

        return self.parse_element()

    def parse_port(self):
        ret = False
        for i in _return_args(self.fn[1:]):
            a, v = _get_argval(i)
            if a in PORT_ARGS:
                self.parsed.update({a: v})
                ret = True

        return ret

    def parse_element(self):
        ret = False
        for i in _return_args(self.fn[1:]):
            a, v = _get_argval(i)
            if a in FILENAME_ARGS:
                self.parsed.update({a: v})
                ret = True

        return ret

def _return_args(split_name):
    return filter(lambda x: ARG_SEPERATOR in x, split_name)

def _get_argval(str_in):
        arg, _, value = str_in.partition(ARG_SEPERATOR)
        return arg, value

def _split_name(filename) -> list:
    spl_char = '_' if '_' in filename else ' '
    return filename.split(spl_char)
