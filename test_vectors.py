#!/usr/bin/env python3

import unittest
import vectors

class TestVectors(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.v = vectors.Vector(1, 2, 3)
        self.u = vectors.Vector(7, 4, 2)

    def tearDown(self):
        super().tearDown()

    def test_init(self):
        self.assertEqual(self.v.x, 1)
        self.assertEqual(self.v.y, 2)
        self.assertEqual(self.v.z, 3)

    def test_equality(self):
        v_copy = vectors.Vector(self.v.x, self.v.y, self.v.z)
        self.assertEqual(self.v, v_copy)

    def test_addition(self):
        self.assertEqual(self.v + self.u,
                         vectors.Vector(8, 6, 5))

    def test_subtraction(self):
        self.assertEqual(self.v - self.u,
                         vectors.Vector(-6, -2, 1))


if __name__ == '__main__':
    unittest.main()
