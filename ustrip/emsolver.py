import numpy as np
import zipfile, tempfile, os, sys, argparse, platform, struct
from openEMS.physical_constants import C0
from openEMS import openEMS
from CSXCAD import ContinuousStructure

from stlimport import StlReader
from geomaker import GeoMaker, SimGeometry
from meshmaker import StripMesher

class EMSolver:
    """EMSolver

            Entry point for openEMS / FDTD simulation utility.

            """

    def __init__(self):
        self.reader    = StlReader()
        self.geomaker  = GeoMaker()
        self.mesher    = StripMesher()

        self.geometry : SimGeometry
        self.sim_path : os.path
        self.fdtd     : openEMS

        self.cf   = 1e09
        self.span = 1e08

    def init_sim(self, cf, span, boundary=['PEC']*6):
        self.cf = cf
        self.span = span
        self.fdtd = openEMS(CellConstantMaterial=False)
        self.fdtd.SetGaussExcite(cf, span / 2)
        self.fdtd.SetBoundaryCond(boundary)
        self.fdtd.SetCSX(self.geometry.csx)

    def run_sim(self, verbose=False, debug_pec=False):
        self.fdtd.Run(self.sim_path, verbose=verbose, debug_pec=debug_pec)

    def run_cadapp(self, sim_path=None):
        os.mkdir(sim_path)
        csx_file = os.path.join(sim_path, 'model.xml')
        self.csx.Write2XML(csx_file)
        os.system('AppCSXCAD "{}"'.format(csx_file))
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



