import numpy as np
from constants import *

class StlDataParser:
    def __init__(self) -> None:
        ...

    def get_bbox(self, data):
        start, stop = None
        for facet in data:
            for v in facet:
                start = v if start is None else np.minimum(v, start)
                stop  = v if stop is None else np.maximum(v, stop)
        return start, stop

    def bbox_corners(self, start, stop) -> np.array:
        ...
        # Project start / stop 'across' space long axis (now two points per bbox face)
        # Project shift start / stop face points up / down.
        # Done

    def is_rectocube(self, shape) -> bool:
        ...

    def get_normal(self, facet) -> np:
        pass

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