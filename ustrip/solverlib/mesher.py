import numpy as np
from CSXCAD import ContinuousStructure
from solverlib.classes import Mesher
from classes import GeoEle, Port
from solverlib.constants import STL_UNIT

# To Do:
# - Where does mesh live?
# - Should mesher class have any properties? 

class Mesher:
    def __init__(self) -> None:
        ...

class BasicMesher(Mesher):

    """ Microstrip Mesher

            Takes CSXCAD input files describing PCB with microstrip geometry and creates mesh.

            Should eventually create inhomogenous mesh via some algorithm.

            I wonder if vertex pairs colinear w/ major axis are consistently 'edges'?
            Might also indicate discontinuity?

            Can probably use normal vector for something more 3D like resonators?
            """

    def __init__(self) -> None:
        self.gunit = STL_UNIT

    def mesh_edges(self, ele: GeoEle, csx: ContinuousStructure):
        ...
    
    def mesh_interior(self, ele: GeoEle, csx: ContinuousStructure):
        ...

    def mesh_lumport(self, port: Port, csx: ContinuousStructure):
        ...

    def mesh_rwgport(self, port: Port, csx: ContinuousStructure):
            ...
    
    def mesh_mslport(self, port: Port, csx: ContinuousStructure):
        ...

    def mesh_substrate(self, ele: GeoEle, csx: ContinuousStructure):
        ...
    
    def mesh_ustrip(self, ele: GeoEle, csx: ContinuousStructure):
        ...






