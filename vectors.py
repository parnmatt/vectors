#!/usr/bin/env python3

from collections import namedtuple
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
