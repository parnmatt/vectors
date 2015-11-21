#!/usr/bin/env python3

import math
import unittest

import vectors

class TestVector(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.v = vectors.Vector(1, 2, 3)
        self.u = vectors.Vector(7, 4, 2)

    def tearDown(self):
        super().tearDown()

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

    def test_ensure_scalar_commutes_mul(self):
        self.assertEqual(self.u * 10.3, 10.3 * self.u)

    def test_squaring(self):
        self.assertEqual(self.v**2, self.v * self.v)

    def test_fractional_powers(self):
        self.assertEqual(round(self.u**5.2, 7),
                         round(math.sqrt(self.u * self.u)**5.2, 7))

    def test_negative_power(self):
        self.assertEqual(self.v**(-3), 1 / self.v**3)

    def test_magnitude(self):
        self.assertEqual(self.v.magnitude(), math.sqrt(14))

    def test_length(self):
        self.assertEqual(self.u.length(), math.sqrt(69))

    def test_vector_div_integer_scalar(self):
        self.assertEqual(self.v / 2, vectors.Vector(0.5, 1.0, 1.5))

    def test_vector_div_decimal_scalar(self):
        self.assertEqual(self.u / 2.5, vectors.Vector(2.8, 1.6, 0.8))

    def test_vector_div_vector(self):
        with self.assertRaises(TypeError):
            self.v / self.u

    def test_unit_vector(self):
        self.assertEqual(self.v.unit(), self.v / self.v.magnitude())

    def test_pos_vector(self):
        self.assertEqual(+self.v, self.v)

    def test_neg_vector(self):
        self.assertEqual(-self.u, vectors.Vector(-7, -4, -2))

class TestVector3(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.v = vectors.Vector3(1, 2, 3)
        self.u = vectors.Vector3(7, 4, 2)
        self.w = vectors.Vector3(2, 2*math.sqrt(3), 3)

    def tearDown(self):
        super().tearDown()

    def test_get_x(self):
        self.assertEqual(self.u.x, 7)

    def test_get_y(self):
        self.assertEqual(self.u.y, 4)

    def test_get_z(self):
        self.assertEqual(self.u.z, 2)

    def test_vector_product(self):
        self.assertEqual(vectors.Vector3.vector_product(self.v, self.u),
                         vectors.Vector3(-8, 19, -10))

    def test_cross(self):
        self.assertEqual(vectors.Vector3.cross(self.v, self.u),
                         vectors.Vector3(-8, 19, -10))

    def test_vector_product_anticommutes(self):
        self.assertEqual(vectors.Vector3.vector_product(self.v, self.u),
                         -vectors.Vector3.vector_product(self.u, self.v))

    def test_spherical_polar_radius(self):
        self.assertEqual(self.w.r, 5)

    def test_azimuthal_angle(self):
        self.assertEqual(round(self.w.phi * 180/math.pi, 7), 60)

    def test_zenith_angle(self):
        self.assertEqual(math.cos(self.w.theta), 3/5)

    def test_cylindrical_polar_radius(self):
        self.assertEqual(self.w.rho, 4)

if __name__ == '__main__':
    unittest.main()
