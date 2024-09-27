import numpy as np
from CSXCAD import ContinuousStructure

class StripMesher:
    
    """ Microstrip Mesher
            
            Takes CSXCAD input files describing PCB with microstrip geometry and creates mesh.
            
            Should eventually create inhomogenous mesh via some algorithm."""
    
    def __init__(self, csx_grid, wavelen=None) -> None:
        # Sim Geometry Bounding Boxes
        self.ustrip    = None
        self.substrate = None
        self.gnd_plane = None

        # Meshing Calculation Vars
        self.wavelen   = wavelen
        self.perm_eff  = 3.0
        self.gunit     = 1e-3 
        self.scale     = 1.0
      
        # Mesh Outputs CSX CAD
        self.mesh      = csx_grid
        self.mesh.SetDeltaUnit(self.gunit)

    def add_ustrip(self, start, stop):
        self.ustrip = start, stop
    
    def add_substrate(self, sub, perm):
        self.substrate = sub
        self.perm_eff  = perm
    
    def add_gnd(self, start, stop):
        self.gnd_plane = start, stop

    def mesh_ustrip(self):
        pass
    
    def mesh_substrate(self):
        pass

    def mesh_gnd(self):
        pass




