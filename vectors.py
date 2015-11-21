#!/usr/bin/env python3

from collections import namedtuple
import itertools as it
import numbers
import operator as op

class Vector3(namedtuple('Vector3', ('x', 'y', 'z'))):
    """A 3-dimensional mathematical vector."""
    pass

class Vector(tuple):
    """An n-dimensional mathematical vector."""

    def __new__(self, *components):
        """Create a tuple of the components."""
        return tuple.__new__(self, components)

    def __repr__(self):
        """Return string that can be reevaluated."""
        return self.__class__.__name__ + super().__repr__()

    __str__ = __repr__

    @classmethod
    def _map(cls, func, *iterables):
        """Map function over the components."""
        return cls(*map(func, *iterables))

    def __add__(self, v):
        """Add the components of the vectors."""
        return self._map(op.add, self, v)

    def __sub__(self, v):
        """Subtract the components of the vectors."""
        return self._map(op.sub, self, v)

    @staticmethod
    def scalar_product(v, u):
        """Scalar (dot) product of the vectors."""
        return sum(map(op.mul, v, u))

    dot = scalar_product

    def __mul__(self, v):
        """Return scaled vector     if v is a scalar,
                  scalar product    if v is a vector
        """
        if isinstance(v, numbers.Number):
            return self._map(op.mul, self, it.repeat(v))
        else:
            return self.scalar_product(self, v)

    __rmul__ = __mul__

    def __pow__(self, power):
        """Return vector magnitude to given power."""
        return (self * self)**(power/2)

    def magnitude(self):
        """Returns the magnitude of the vector."""
        return self**1

    length = magnitude

    def __truediv__(self, scalar):
        """Return vector scaled by the reciprocal of the scalar."""
        if isinstance(scalar, numbers.Number):
            return self._map(op.truediv, self, it.repeat(scalar))
        else:
            raise TypeError

    def unit(self):
        """Return corresponding unit vector."""
        return self / self.magnitude()

    def __pos__(self):
        """Return vector unchanged."""
        return self

    def __neg__(self):
        """Negate vector."""
        return -1 * self

