#!/usr/bin/env python3

from collections import namedtuple

class Vector(namedtuple('Vector', ('x', 'y', 'z'))):
    """A 3-dimensional mathematical vector."""

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
