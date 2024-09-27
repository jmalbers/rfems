import numpy as np
from CSXCAD import ContinuousStructure

class StripMesher:
    
    """ Microstrip Mesher
            
            Takes CSXCAD input files describing PCB with microstrip geometry and creates mesh.
            
            Should  eventually create inhomogenous mesh via some algorithm."""
    
    def __init__(self, csx_features: list[2], wavelen=None, scale=1.0) -> None:
        # Sim Geometry CSXCAD
        self.ustrip    = csx_features[0]
        self.substrate = csx_features[1]
        self.gnd_plane = csx_features[2]

        # Calc Vars
        self.wavelen   = wavelen
        self.scale     = scale
      
        # Mesh Outputs CSX CAD
        self.mesh      = None


