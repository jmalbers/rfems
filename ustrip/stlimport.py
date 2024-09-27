
import numpy as np
import zipfile, tempfile, os, sys, argparse, platform, struct

class StlImporter:
    """ STL Importer
    
        Imports STL geometries and materials data for use with EM Solver / openEMS
        
        
        """
    
    def __init__(self) -> None:
        self.stl_data  = None
        self.materials = None
        self.priority  = None
        
        
    def parse_stl(self, filename):
        data = []
        with open(filename, 'rb') as fp:
            header = fp.read(5)
            if header == b'solid':
                facet = [] 
                for ln in fp:
                    d = ln.split()
                    if d[0] == b'endfacet' and facet:
                        data.append(np.array(facet))
                        facet = []
                    if d[0] == b'vertex' and len(d) == 4:
                        facet.append([ float(x) for x in d[1:] ])
            else:
                raise ValueError('binary stl files unsupported: not enough precision')
        return data

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
        return data