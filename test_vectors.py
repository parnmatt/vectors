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
        self.assertEqual(self.v, vectors.Vector._make(self.v))

    def test_addition(self):
        self.assertEqual(self.v + self.u,
                         vectors.Vector(8, 6, 5))

    def test_subtraction(self):
        self.assertEqual(self.v - self.u,
                         vectors.Vector(-6, -2, 1))

    def test_scalar_product(self):
        self.assertEqual(vectors.Vector.scalar_product(self.v, self.u), 21)

    def test_dot_product(self):
        self.assertEqual(vectors.Vector.dot(self.v, self.u), 21)

    def test_vector_mul_vector(self):
        self.assertEqual(self.v * self.u, 21)

    def test_vector_mul_scalar(self):
        self.assertEqual(self.v * 5, vectors.Vector(5, 10, 15))

    def test_scalar_mul_vector(self):
        self.assertEqual(3 * self.u, vectors.Vector(21, 12, 6))

if __name__ == '__main__':
    unittest.main()
