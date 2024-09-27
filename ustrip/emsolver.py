import numpy as np
import zipfile, tempfile, os, sys, argparse, platform, struct
from openEMS.physical_constants import C0
from openEMS import openEMS
from CSXCAD import ContinuousStructure

from stlimport import StlImporter
from stripmesher import StripMesher

class EMSolver:
    """EMSolver
            
            Entry point for EMS / FDTD simulation utility using openEMS and CSXCAD
            
            """
    
    def __init__(self):
        self.importer = StlImporter()
        self.mesher   = StripMesher()

        self.fdtd     : openEMS
        self.geometry : Geometry
        self.sim_path : os.path

    def init_sim(self, cf, span, boundary=['PEC']*6):
        self.fdtd = openEMS(CellConstantMaterial=False)
        self.fdtd.SetGaussExcite(cf, span / 2)
        self.fdtd.SetBoundaryCond(boundary)
        self.fdtd.SetCSX(self.geometry.csx)

    def run_sim(self, verbose=False, debug_pec=False):
        self.fdtd.Run(self.sim_path, verbose=verbose, debug_pec=debug_pec)

    def run_cadapp(self, sim_path=None):
        os.mkdir(sim_path)
        CSX_file = os.path.join(sim_path, 'model.xml')
        self.csx.Write2XML(CSX_file)
        os.system('AppCSXCAD "{}"'.format(CSX_file))
        sys.exit(0)

    def run_paraview(self):
        os.system('paraview "PEC_dump.vtp"')
        sys.exit(0)

    def save_results(self, filename, f, s, z, ff):
        root, ext = os.path.splitext(filename)
        if ext != '.npz':
            filename = f'{root}.npz'
        np.savez(filename, f=f, s=s, z=z, **ff)

    def _calc_scattering(self):
        pass

    def _cal_ports(self):
        pass  

class Geometry:
    def __init__(self):
        self.csx = ContinuousStructure()
        self.mesh = None
        self.ports = []

class MicroStrip(Geometry):
    def __init__(self) -> None:
        self.sub_perm = None
        self.sub_xyz  = None
        self.cond_mat = None
        
