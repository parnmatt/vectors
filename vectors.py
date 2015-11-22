#!/usr/bin/env python3

from collections import namedtuple
import functools as ft
import math
import numbers
import operator as op

class VectorLengthError(ArithmeticError):
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

    @staticmethod
    def _same_length(*iterables):
        """Return True if all iterables are the same length."""
        return ft.reduce(op.eq, map(len, iterables))

    @classmethod
    def _map(cls, func, *iterables):
        """Map function over the components."""
        if cls._same_length(*iterables):
            return cls(*map(func, *iterables))
        else:
            raise VectorLengthError('Given vectors are not the same length')

    @classmethod
    def scalar_product(cls, v, u):
        """Scalar (dot) product of the vectors."""
        return sum(cls._map(op.mul, v, u))

    dot = scalar_product

    def __mul__(self, v):
        """Return scaled vector     if v is a scalar,
                  scalar product    if v is a vector
        """
        if isinstance(v, numbers.Number):
            v = [v] * len(self)
            return self._map(op.mul, self, v)
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
            v = [scalar] * len(self)
            return self._map(op.truediv, self, v)
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

    def __add__(self, v):
        """Add the components of the vectors."""
        return self._map(op.add, self, v)

    __radd__ = __add__

    def __sub__(self, v):
        """Subtract the components of the vectors."""
        return self._map(op.sub, self, v)

    def __rsub__(self, v):
        return -self + v

    def dimension(self):
        """Returns the dimension on the vector."""
        return len(self)


class Vector3(namedtuple('_Vector3', ('x', 'y', 'z')), Vector):
    """A 3-dimensional mathematical vector."""

    @classmethod
    def vector_product(cls, v, u):
        """Return the vector product of the given vectors."""
        return cls(x=v.y*u.z - u.y*v.z,
                   y=v.z*u.x - u.z*v.x,
                   z=v.x*u.y - u.x*v.y)

    cross = vector_product

    @property
    def r(self):
        """Return the spherical polar radius."""
        return self.magnitude()

    @property
    def phi(self):
        """Return the azimuthal angle."""
        return math.atan2(self.y, self.x)

    @property
    def theta(self):
        """Return the zenith angle."""
        return math.acos(self.z/self.r)

    @property
    def rho(self):
        """Return the cylindrical polar radius."""
        return self.r * math.sin(self.theta)

class LorentzVector(namedtuple('_LorentzVector',
                               ('t',) + Vector3._fields), Vector3):
    """A 1+3 Lorentz Vector, of the form (t, x, y, z)."""
    pass
