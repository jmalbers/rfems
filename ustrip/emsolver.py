import numpy as np
import tempfile, os, sys, argparse
from openEMS.physical_constants import C0
from openEMS import openEMS

from stlimport import StlReader
from geomaker import GeoMaker, SimGeometry
from meshmaker import StripMesher
from solverlib.constants import *
from solverlib.classes import *

class EMSolver:
    """EMSolver

            Entry point for openEMS / FDTD simulation utility.

            """

    def __init__(self):
        self.maker  : Maker
        self.mesher : Mesher
        self.reader : Importer

        self.geometry : SimGeometry
        self.sim_path : os.path
        self.fdtd     : openEMS

        self.cf   = None
        self.span = None
        self.lam  = None

    def config_EMSolver(self):
        if self.lam is None:
            raise RuntimeError("Frequency sweep parameters not set.")

        self.maker  = GeoMaker(USTRIP)
        self.mesher = StripMesher(self.cf + (self.span / 2))
        self.reader = StlReader()

    def config_FDTD(self, boundary=USTRIP_BOUNDARY):
        self.fdtd = openEMS(CellConstantMaterial=False)
        self.fdtd.SetGaussExcite(self.cf, self.span / 2)
        self.fdtd.SetBoundaryCond(boundary)
        self.fdtd.SetCSX(self.geometry.csx)

    def set_sweep(self, cf, span):
        if cf - span < 5e08:
            raise ValueError(f"500MHz isn't RF!")
        self.cf   = cf
        self.span = span
        self.lam  = C0 / (self.cf + span)

    def load_zip(self, filename):
        if _file_ok(filename):
            self.reader.import_file(filename)

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

def _file_ok(filename) -> bool:

    for x in filename.split():
        if x in STRUCTURES:
            return True

    return False




