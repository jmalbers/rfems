# EMSolver Constants

# Boundary Conditions
PEC   = 'pec'
MUR   = 'mur'
PMC   = 'pmc'
PML_8 = 'pml_8'
BOUNDARY_CONDITIONS = [PEC, MUR, PMC, PML_8]
USTRIP_BOUNDARY = PEC * 6

# Simulation Args
END_CRITERIA  = 'EndCriteria'
NUM_TIMESTEPS = 'NrTS'
PRIORITY      = 'priority'
Z0            = 'zo'
KAPPA         = 'kappa'
EPSILON       = 'epsilon'
FILENAME_ARGS = [PRIORITY, Z0, KAPPA, EPSILON]

# 3D Model Elements
MSL_PORT  = 'mslport'
RWG_PORT  = 'rwgport'
LUM_PORT  = 'lumport'
USTRIP    = 'ustrip'
SUBSTRATE = 'substrate'
DUMP_BOX  = 'dumpbox'
ENCLOSURE = 'enclosure'
PART      = 'part'
WIRE      = 'wire'
VALID_PARTS = [USTRIP, SUBSTRATE, MSL_PORT, RWG_PORT, LUM_PORT,
               DUMP_BOX, ENCLOSURE, PART, WIRE]

# STL Constants
STL_TOL = .001  # mm
STL_UNIT = 1e-3

# SIM Constants
DEFAULT_PITCH     = 1e-3
DEFAULT_POINTS    = 1000  # even to ensure group delay calculation
DEFAULT_REFERENCE = 50
DEFAULT_PRIORITY  = 0
DEFAULT_DPHI      = 2
DEFAULT_DTHETA    = 2

# METALS
SILVER   = 'silver'
COPPER   = 'copper'
GOLD     = 'gold'
ALUMINUM = 'aluminum'
BRASS    = 'brass'
STEEL    = 'steel'
METALS = [SILVER, COPPER, GOLD, ALUMINUM, BRASS, STEEL]

KAPPAS = {  # s/m
    SILVER:   62.1e6 ,
    COPPER:   58.7e6,
    GOLD:     44.2e6,
    ALUMINUM: 36.9e6,
    BRASS:    15.9e6,
    STEEL:    10.1e6,
}

# Colors
COLORS = {
    PEC:      "#dbc7b8",
    SILVER:   "#c0c0c0",
    COPPER:   "#e6be8a",
    GOLD:     "#ffd700",
    ALUMINUM: "#d0d5d9",
    BRASS:    "#ac9f3c",
    STEEL:    "#888b8d",
}

# Directions
X   = 'x'
Y   = 'y'
Z   = 'z'
XYZ = 'xyz'
YZ  = 'yz'
XZ  = 'xz'
XY  = 'xy'

DIRECTIONS = {
    X: '0',
    Y: '1',
    Z: '2',
}
