import numpy as np
import zipfile, tempfile, os, logging, warnings
from io import BytesIO
from solverlib.classes import Importer
from solverlib.constants import *

STL_HEADER_SIZE = 80
STL_EOL = '\r\n'

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
        self.temp    : tempfile.TemporaryDirectory
        self.logger  = logging.getLogger(__class__.__name__)

    def import_zip(self, filename):
        self.logger.info(f"* Importing ZIP file '{filename}'")
        self._unzip_models(filename)

        for r, _, f in os.walk(self.temp.name):
            for name in f:
                imp = self.import_stl(os.path.join(r, name))
                imp.stl_data = self._make_npdata(imp.stl_byio)
                self.imports.append(imp)

        self.temp.cleanup()

    def import_stl(self, filename):
        self.logger.info(f'\n* Importing STL file "{filename}" *')
        imp = ImportedStl()
        imp.filename = os.path.splitext(os.path.split(filename)[1])[0]

        with open(filename, 'rb') as f:
            if f.read(5) != b'solid':
                raise ValueError(f"'{filename}' is unsupported STL format.")
            f.seek(0)
            imp.stl_byio = BytesIO(f.read())

        if len(imp.stl_byio.readline()) != 80: 
            self._fix_header(imp.stl_byio)

        imp.stl_byio.seek(0)
        return imp

    def _make_npdata(self, stl_byio: BytesIO):
        self.logger.info('\n* Making numpy data from STL import *')
        data  = []
        facet = []

        f = stl_byio
        for ln in f:
            self.logger.debug(f' Making numpy data from: {ln}')
            d = ln.split()

            if d[0] == b'endfacet' and facet:
                data.append(np.array(facet))
                facet = []
            if d[0] == b'vertex' and len(d) == 4:
                facet.append([ float(x) for x in d[1:]])
        f.seek(0)

        return data

    def _unzip_models(self, filename):
        zip = zipfile.ZipFile(filename)
        self.temp = tempfile.TemporaryDirectory()

        for info in zip.infolist():
            if info.is_dir():
                continue
            root, ext = os.path.splitext(info.filename)
            if ext == '.stl':
                zip.extract(info, path=str(self.temp.name))

    def _fix_header(self, stl_byio):
        stl_byio.seek(0)
        stl = stl_byio.readlines()
        ln = stl[0].decode()
        self.logger.info(f'\n* Repairing STL header line length: {len(ln)} *')
        self.logger.debug(f'\n STL header value: {ln}')
        eol = ln.find(STL_EOL)
        pad = STL_HEADER_SIZE - len(ln)
        fixln = f'{ln[:eol]}{" " * pad}{STL_EOL}'.encode()
        self.logger.debug(f' \nNew STL header line length: {len(fixln)}'
                          f' \nNew STL header value: {fixln}')
        stl_byio.seek(0)
        stl_byio.write(fixln)
        for idx in range(1, len(stl)-1):
            stl_byio.write(stl[idx])
        stl_byio.seek(0)
                         
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

        if fn[0] not in ELEMENTS:
            raise TypeError(f"'{fn}' is invalid sim element.")

        arg_list = []
        parsed = {}
        parsed.update({ELEMENT: fn[0]})

        if parsed[ELEMENT] in PORTS:
            arg_list = PORT_ARGS
        else: 
            arg_list = FILENAME_ARGS

        for i in self._return_args(fn[1:]):
            a, v = self._get_argval(i)
            if a in arg_list:
                parsed.update({a: v})
            else:
                warnings.warn(f"'{a}={v}' is invalid simulation element argument.")

        return parsed

    def _return_args(self, split_name):
        return list(filter(lambda x: ARG_SEPERATOR in x, split_name))

    def _get_argval(self, str_in):
        arg, _, value = str_in.partition(ARG_SEPERATOR)
        return arg, value

    def _split_name(self, filename) -> list:
        spl_char = '_' if '_' in filename else ' '
        return filename.split(spl_char)
