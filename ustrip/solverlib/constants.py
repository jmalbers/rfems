# EMSolver Constants

# Boundary Conditions
PEC = 'pec'
MUR = 'mur'
PMC = 'pmc'
PML_8 = 'pml_8'
USTRIP_BOUNDARY = PEC * 6
CAVITY_BOUNDARY = PEC * 6

# Simulation Args
END_CRITERIA = 'EndCriteria'
NUM_TIMESTEPS = 'NrTS'
PRIORITY = 'priority'
Z0 = 'zo'
KAPPA = 'kappa'
EPSILON = 'epsilon'
FILENAME_ARGS = PRIORITY, Z0, KAPPA, EPSILON

# 3D Model Elements
PORT = 'port'
USTRIP = 'ustrip'
SUBSTRATE = 'substrate'
MODEL_PARTS = USTRIP, SUBSTRATE, PORT

# STL Constants
STL_TOL = .001  # mm
STL_UNIT = 1e-3

# SIM Constants
DEFAULT_PITCH = 1e-3
DEFAULT_POINTS = 1000  # even to ensure group delay calculation
DEFAULT_REFERENCE = 50
DEFAULT_PRIORITY = 0
DEFAULT_DPHI = 2
DEFAULT_DTHETA = 2

# Materials
MATERIALS = {  # s/m
    'silver':   { "kappa": 62.1e6 },
    'copper':   { "kappa": 58.7e6 },
    'gold':     { "kappa": 44.2e6 },
    'aluminum': { "kappa": 36.9e6 },
    'brass':    { "kappa": 15.9e6 },
    'steel':    { "kappa": 10.1e6 },
}

# Colors
COLORS = {
    "pec":      "#dbc7b8",
    "silver":   "#c0c0c0",
    "copper":   "#e6be8a",
    "gold":     "#ffd700",
    "aluminum": "#d0d5d9",
    "brass":    "#ac9f3c",
    "steel":    "#888b8d",
}

# Directions
X = 'x'
Y = 'y'
Z = 'z'

XYZ = 'xyz'
YZ  = 'yz'
XZ  = 'xz'
XY  = 'xy'

DIRECTIONS = {
    X: '0',
    Y: '1',
    Z: '2',
}
