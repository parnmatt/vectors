#!/usr/bin/env python3

from collections import namedtuple
import itertools as it
import numbers
import operator as op

class Vector(namedtuple('Vector', ('x', 'y', 'z'))):
    """A 3-dimensional mathematical vector."""

    @classmethod
    def _map(cls, func, *iterables):
        """Map function over the components."""
        return cls._make(map(func, *iterables))

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

