import numpy as np
import zipfile, tempfile, os, sys, argparse, platform, struct
from openEMS.physical_constants import C0
from openEMS import openEMS
from CSXCAD import ContinuousStructure

from stlimport import StlImporter
from stripmesher import StripMesher

class EMSolver:
    def __init__(self):
        self.importer = StlImporter()
        self.mesher   = StripMesher()

        self.csx  = None
        self.fdtd = None
        self.sim_path = None

    def init_sim(self, cf, span, boundary=['PEC']*6):
        self.csx = ContinuousStructure()
        fdtd = openEMS(CellConstantMaterial=False)
        fdtd.SetGaussExcite(cf, span / 2)
        fdtd.SetBoundaryCond(boundary)
        fdtd.SetCSX(self.csx)

    def run_sim(self, verbose=False, debug_pec=False):
        self.fdtd.Run(self.sim_path, verbose=verbose, debug_pec=debug_pec)

    def run_appcsxcad(self, sim_path=None):
        os.mkdir(sim_path)
        CSX_file = os.path.join(sim_path, 'model.xml')
        self.csx.Write2XML(CSX_file)
        os.system('AppCSXCAD "{}"'.format(CSX_file))
        sys.exit(0)

    def run_paraview(self):
        os.system('paraview "PEC_dump.vtp"')
        sys.exit(0)

    

class Ustrip2p:
    def __init__(self) -> None:
        self.cond  = None
        self.perm  = None
        self.mesh  = None
        self.port1 = None
        self.port2 = None