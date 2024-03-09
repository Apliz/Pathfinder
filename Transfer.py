"""Transfer Class"""
from math import sqrt
from constants import GM
from Orbit import Orbit

# Not yet integrated into Flask.
# Not yet hooked up to the database

class Transfer(Orbit):
    """Instance of an orbital transfer within Earth's orbit"""

    def __init__(self, departure_orbit, arrival_orbit):
        self.departure_orbit = departure_orbit
        self.arrival_orbit = arrival_orbit
        
    def a_transfer(self):
        """return the semi-major axis of a transfer orbit"""
        r1 = self.departure_orbit.radius_at("apogee")
        r2 = self.arrival_orbit.radius_at("perigee")
        return (r1+r2) / 2

    def hohmann_transfer(self):
        """Returns total deltaV for a hohmann transfer manoeuvre in `km s-1`"""
        v1 = self.departure_orbit.velocity_at_position("apogee")
        v2 = self.arrival_orbit.velocity_at_position("perigee")
        vt1 = sqrt(2*((GM / self.departure_orbit.radius_at("apogee")) + (-abs(GM) / (2 * self.a_transfer()))))
        vt2 = sqrt(2*((GM / self.arrival_orbit.radius_at("perigee" )) + (-abs(GM) / (2 * self.a_transfer()))))

        delta_v1 = vt1 - v1
        delta_v2 = vt2 - v2

        total_delta_v = delta_v1 + delta_v2
        return total_delta_v
   