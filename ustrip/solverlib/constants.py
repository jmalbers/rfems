# ---------------------------------------
# EMSolver Constants
# ---------------------------------------

DEFAULT_PITCH     = 1e-3
DEFAULT_POINTS    = 1000  # even to ensure group delay calculation
DEFAULT_REFERENCE = 50
DEFAULT_PRIORITY  = 0
DEFAULT_DPHI      = 2
DEFAULT_DTHETA    = 2

    # Boundary Conditions

PEC   = 'pec'
MUR   = 'mur'
PMC   = 'pmc'
PML_8 = 'pml_8'
BOUNDARY_CONDITIONS = [PEC, MUR, PMC, PML_8]
USTRIP_BOUNDARY = PEC * 6

# ------------------------------------------------------------------------------
# 3D Model Constants
# ------------------------------------------------------------------------------

# STL Constants

STL_TOL = .001  # mm
STL_UNIT = 1e-3

# Geometry ID Constants
     
     # Ports
PORT      = 'port'
RWG_PORT  = 'rwgport'
LUM_PORT  = 'lumport'
MSL_PORT  = 'mslport'

    # Boxes
DUMP_BOX  = 'dumpbox'
MESH_BOX  = 'meshbox'

    # Misc.
ELEMENT   = 'element'
USTRIP    = 'ustrip'
SUBSTRATE = 'substrate'
ENCLOSURE = 'enclosure'
PART      = 'part'
WIRE      = 'wire'

    # Classifications
ELEMENTS = [USTRIP, SUBSTRATE, PORT, RWG_PORT, LUM_PORT,
            DUMP_BOX, ENCLOSURE, PART, WIRE]
PORTS    = [RWG_PORT, LUM_PORT, MSL_PORT]
BOXES    = [DUMP_BOX, MESH_BOX]



# ------------------------------------------------------------------------------
# Metal Constants
# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------
# Color Constants
# ------------------------------------------------------------------------------

RED    = 'red'
BLUE   = 'blue'
GREEN  = 'green'
YELLOW = 'yellow'
ORANGE = 'orange'
WHITE  = 'white'
BLACK  = 'black'
GREY   = 'grey'

    # Material & Structure Color Definition

COLORS = {
    PEC:       "#dbc7b8",
    SILVER:    "#c0c0c0",
    COPPER:    "#e6be8a",
    GOLD:      "#ffd700",
    ALUMINUM:  "#d0d5d9",
    BRASS:     "#ac9f3c",
    STEEL:     "#888b8d",
    USTRIP:    "#b87333",
    SUBSTRATE: "#efdfbb",
    RWG_PORT:  "#56a0d3",
    RED:       "#ff0000",
    BLUE:      "#00bfff",
    GREEN:     "#4d5d53",
    YELLOW:    "#ffe135",
    WHITE:     "#ffffff",
    BLACK:     "#000000",
    GREY:      "#8A8A8A"
}

# ------------------------------------------------------------------------------
# Directions Constants
# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------
# Simulation Argument Constants
# ------------------------------------------------------------------------------

ARG_SEPERATOR = '='
END_CRITERIA  = 'EndCriteria'
NUM_TIMESTEPS = 'NrTS'
PRIORITY      = 'pri'
Z0            = 'zo'
KAPPA         = 'kappa'
EPSILON       = 'epsilon'
NUMBER        = 'n'
DIRECTION     = 'd'
EXCITE        = 'excite'
MATERIAL      = 'mat'
TE10          = 'te10'
COLOR         = 'color'

    # Argument Classifications

FILENAME_ARGS = [PRIORITY, Z0, KAPPA, EPSILON, NUMBER, DIRECTION, MATERIAL,
                 EXCITE, COLOR]
PORT_ARGS     = [Z0, NUMBER, DIRECTION, EXCITE]

    # Default Material Priorities Definition

PRIORITIES = {
    RWG_PORT: '',
    MSL_PORT: '',
    LUM_PORT: '',
    SUBSTRATE: '',
    USTRIP: '',
}