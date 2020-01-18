from vpython import vector, color, sqrt, sphere, rate, scene
from math import fsum
from random import gauss
import numpy as np

# CONSTANTS


# Universal gravitational constant
G = 6.673e-11

scene.width = 1300
scene.height = 650

# Solar mass in kg (assume average stellar mass)
SOLAR_MASS = 2.000e30

# Precalculated bounds to solar mass
MIN_SOLAR_MASS = SOLAR_MASS * 0.5
MAX_SOLAR_MASS = SOLAR_MASS * 250
AVG_SOLAR_MASS = SOLAR_MASS * 3.0

# Scale distances for galactic scales
DIST_SCALE = 1e20  # 1e20

# Galactic parameters
MAX_ORBITAL_RADIUS = DIST_SCALE * 10
MIN_ORBITAL_RADIUS = DIST_SCALE * 0.15

MILKY_WAY_GALAXY_THICKNESS = DIST_SCALE * 0.9
ANDROMEDA_GALAXY_THICKNESS = DIST_SCALE * 0.2


# Milky Way contains about 300 billion stars
NUM_STARS_MILKY_WAY = 700
# Andromeda Galaxy contains about 1 trillion (10^12) stars
NUM_STARS_ANDROMEDA = 1400

# Graphical constants
STAR_RADIUS = 0.025
dt = 1e17


# FUNCTIONS

# Limit x between lower and upper
def clamp(x, lower, upper):
    return max(min(x, upper), lower)


# Return the force due to gravity on an object
def gravity(mass1, mass2, radius):
    return G * mass1 * mass2 / radius**2


# Return the acceleration due to gravity on an object.
def g_accel(mass, radius):
    # Limit minimum radius to avoid flinging out too many particles
    radius = max(radius, MIN_ORBITAL_RADIUS)
    return G * mass / radius / radius


# Calculate acceleration on an object caused by galaxy
def accel(obj, galaxy):
    r_galaxy = galaxy.pos - obj.pos
    # We have a = F / m = G * m_center / r ^2
    return r_galaxy.norm() * g_accel(galaxy.mass, r_galaxy.mag)
