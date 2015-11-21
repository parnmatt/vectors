#!/usr/bin/env python3

class Vector():
    """A 3-dimensional mathematical vector."""

    def __init__(self, x, y, z):
        """Initialise with Cartesian coordinates."""
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, v):
        """Vectors are equal if they have the same components."""
        return self.x == v.x and self.y == v.y and self.z == v.z

    def __add__(self, v):
        """Add the components of the vectors."""
        return Vector(self.x + v.x,
                      self.y + v.y,
                      self.z + v.z)

    def __sub__(self, v):
        """Subtract the components of the vectors."""
        return Vector(self.x - v.x,
                      self.y - v.y,
                      self.z - v.z)
