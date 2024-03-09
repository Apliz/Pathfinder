
import math
import matplotlib.pyplot as plt
import json
from fractions import Fraction

# acceleration of Gravity on the surface of the Earth (m/s)
g = 9.81
# Radius of the Earth (m)
R = 6378000
# Standard Gravitational Parameter
Gm = 3.986004418*10**14

f = open("./lib/JSON/orbital_data.json")
orbitalJSON = json.load(f)
f.close()


#This is the start of the calculation that will eventually
# 1. Align all orbits (eccentricities included) at a given point (for example the semi-major-axis)
# 2. Return a sorted list of all heights at a point of all bodies on which pyplot can check distribution.


# Goes through all bodies and calculates the semi-major axis (Assuming perfectly round orbits.)
def semi_major_axis():
  bodies = []

  #go through all orbital bodies
  for i in orbitalJSON:
    
    # get its mean motion
    n = i["MEAN_MOTION"]

    #convert mean motion (n) to usable radians/second
    radians_per_second = n * ((2*math.pi)/86400)

    # calculate semi-major axis of body
    a = Gm**Fraction(1,3) / radians_per_second**Fraction(2,3)

    #format
    print(f'{math.floor(a/10**3)}Km')

    return math.floor(a)


# deltaV calculation for a Hohmann transfer between 2 perfectly circular orbits
def hohmann(R, g,r1,r2) :
  gR2=g*R**2

  # Get the semi major axis (USE FUCNTION - DEFUNCT FOR NOW)
  # semi_major_axis = (r1+r2)/2

  #Calculate transfer velocity needed at apogee and perigee (m/s)
  vTransfer_perigee = math.sqrt(gR2*((2.0/r1)-(2.0/(r1+r2))))
  vTransfer_apogee = math.sqrt(gR2*((2.0/r2)-(2.0/(r1+r2))))

  #Calculate velocities of circular orbits (Start, target) (m/s)
  vCircular_1 = math.sqrt(gR2/r1)
  vCircular_2 = math.sqrt(gR2/r2)

  # Total needed burns at perigee and apogee to complete insertion into new orbit
  perigee_burn = vTransfer_perigee-vCircular_1
  apogee_burn = vCircular_2-vTransfer_apogee

  #Total deltaV
  total_deltaV = perigee_burn + apogee_burn

  return total_deltaV

# print(hohmann(R,g,6.7*10**6,42.24*10**6))


