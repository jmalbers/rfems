import numpy as np
from constants import *

class StlProcessor:
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

class FilenameParser:
    def __init__(self) -> None:
        ...
    
    def get_material(self, filename):
        for i in filename.split():
            if i in MATERIALS.keys():
                return i
    def get_portdir(self, filename):
        for i in filename.split():
            if i in DIRECTIONS.keys():
                return i

    def get_zo(self, filename):
        return int(_get_arg(filename.split(), Z0, '='))

    def get_priority(self, filename) -> int:
        return int(_get_arg(filename.split(), PRIORITY, '='))

    def is_port(self, filename):
        return True if PORT in filename else False
    
    def is_substrate(self, filename):
        return True if SUBSTRATE in filename else False
    
    def is_ustrip(self, filename):
        return True if USTRIP in filename else False

def _get_arg(str_in, arg, sep):
        arg, _, value = str_in.partition(sep)
        return value