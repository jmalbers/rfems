import numpy as np
from CSXCAD import ContinuousStructure
from solverlib.classes import Mesher
from solverlib.constants import STL_UNIT

class StripMesher(Mesher):

    """ Microstrip Mesher

            Takes CSXCAD input files describing PCB with microstrip geometry and creates mesh.

            Should eventually create inhomogenous mesh via some algorithm.

            I wonder if vertex pairs colinear w/ major axis are consistently 'edges'?
            Might also indicate discontinuity?

            Can probably use normal vector for something more 3D like resonators?
            """

    def __init__(self, fmax) -> None:
        # Sim Geometry Bounding Boxes
        self.ustrip    = None
        self.substrate = None

        # Meshing Calculation Vars
        self.fmax      = fmax
        self.perm      = 3.0
        self.grid_unit = STL_UNIT

    def mesh_geo(self, geo):
        ...

    def mesh_ustrip(self):
        pass

    def mesh_substrate(self):
        pass




