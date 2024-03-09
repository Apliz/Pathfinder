"""Orbit Class"""
from math import pi, sqrt
from math import floor
from fractions import Fraction as frac
from constants import GM

class Orbit():
    """Instance of an orbit around Earth"""
    def __init__(self, mean_motion, eccentricity):
        self.mean_motion = mean_motion
        self.eccentricity = eccentricity
        self.a = self.calculate_semi_major_axis()

    def calculate_semi_major_axis(self) -> int:
        """Returns the semi major axis of the orbit in `km`"""
        radians_per_second = self.mean_motion * ((2*pi)/86400)
        semi_major_axis = GM**frac(1,3) / radians_per_second**frac(2,3)
        return floor(semi_major_axis)
    
    def radius_at(self, position:str) -> int:
        """ Returns the orbital radius at a given position in `km`\n

            -> `position` accepts either 'apogee' or 'perigee'
        """
        match position:
            case "apogee":
                return self.a*(self.eccentricity + 1)
            case "perigee":
                return self.a*(1 - self.eccentricity)
        raise NotImplementedError(position)

    def epsilon(self) -> float:
        """Returns the specific orbital energy for an elliptical orbit in `MJ kg-1`"""
        e = -abs(GM) / (2 * self.a)
        return e

    def velocity_at_position(self, ap_or_pe:str) ->int:
        """ Returns velocity of satellite at a given position `Km s-1` \n
            `position` -> The orbital radius 'height' from which instantaneous velocity will be calculated
        """
        v = sqrt(2*((GM / self.radius_at(ap_or_pe)) + self.epsilon()))
        return v

    def orbital_period(self) -> float:
        """Returns the period of an orbit `s`"""
        t = 2*pi*sqrt(pow(self.a, 3) / GM)
        return t
