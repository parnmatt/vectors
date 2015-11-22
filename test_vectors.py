#!/usr/bin/env python3

import math
import unittest

import vectors

class TestVector(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.v = vectors.Vector(4, -6, 7, 2.4, 10)
        self.u = vectors.Vector(2, 3, -0.5, 4, 3)

    def tearDown(self):
        super().tearDown()

    # products
    def test_scalar_product_vector_length_error(self):
        with self.assertRaises(vectors.VectorLengthError):
            vectors.Vector.scalar_product(self.v,
                                          vectors.Vector(1, 2, 3))

    def test_scalar_product_vector_vector(self):
        self.assertEqual(vectors.Vector.scalar_product(self.v, self.u), 26.1)

    def test_scalar_product_vector_tuple(self):
        self.assertEqual(vectors.Vector.scalar_product(self.v,
                                                       (5, 4, 3, 2, 1)), 31.8)

    def test_scalar_product_tuple_vector(self):
        self.assertEqual(vectors.Vector.scalar_product((5, 4, 3, 2, 1),
                                                       self.v), 31.8)

    def test_scalar_product_vector_list(self):
        self.assertEqual(vectors.Vector.scalar_product(self.u,
                                                       [5, 4, 3, 2, 1]), 31.5)

    def test_scalar_product_list_vector(self):
        self.assertEqual(vectors.Vector.scalar_product([5, 4, 3, 2, 1],
                                                       self.u), 31.5)

    def test_dot_vector_vector(self):
        self.assertEqual(vectors.Vector.dot(self.v, self.u), 26.1)

    def test_dot_vector_tuple(self):
        self.assertEqual(vectors.Vector.dot(self.v, (5, 4, 3, 2, 1)), 31.8)

    def test_dot_tuple_vector(self):
        self.assertEqual(vectors.Vector.dot((5, 4, 3, 2, 1), self.v), 31.8)

    def test_dot_vector_list(self):
        self.assertEqual(vectors.Vector.dot(self.u, [5, 4, 3, 2, 1]), 31.5)

    def test_dot_list_vector(self):
        self.assertEqual(vectors.Vector.dot([5, 4, 3, 2, 1], self.u), 31.5)

    def test_vector_mul_vector(self):
        self.assertEqual(self.v * self.u, 26.1)

    def test_vector_mul_tuple(self):
        self.assertEqual(self.v * (5, 4, 3, 2, 1), 31.8)

    def test_tuple_mul_vector(self):
        self.assertEqual((5, 4, 3, 2, 1) * self.v, 31.8)

    def test_vector_mul_list(self):
        self.assertEqual(self.u * [5, 4, 3, 2, 1], 31.5)

    def test_list_mul_vector(self):
        self.assertEqual([5, 4, 3, 2, 1] * self.u, 31.5)

    def test_vector_mul_scalar(self):
        self.assertEqual(self.v * 5, vectors.Vector(20, -30, 35, 12, 50))

    def test_scalar_mul_vector(self):
        self.assertEqual(3 * self.u, vectors.Vector(6, 9, -1.5, 12, 9))

    def test_ensure_scalar_commutes_mul(self):
        self.assertEqual(self.u * 10.3, 10.3 * self.u)

    # exponential
    def test_squaring(self):
        self.assertEqual(self.v**2, self.v * self.v)

    def test_fractional_powers(self):
        self.assertEqual(round(self.u**5.2, 7),
                         round(math.sqrt(self.u * self.u)**5.2, 7))

    def test_negative_power(self):
        self.assertEqual(self.v**(-3), 1 / self.v**3)

    # vector length
    def test_magnitude(self):
        self.assertEqual(self.v.magnitude(), math.sqrt(206.76))

    def test_length(self):
        self.assertEqual(self.u.length(), math.sqrt(38.25))

    # division
    def test_vector_div_integer_scalar(self):
        self.assertEqual(self.v / 2, vectors.Vector(2.0, -3.0, 3.5, 1.2, 5.0))

    def test_vector_div_decimal_scalar(self):
        self.assertEqual(self.u / 2.5, vectors.Vector(0.8, 1.2, -0.2, 1.6, 1.2))

    def test_vector_div_vector(self):
        with self.assertRaises(TypeError):
            self.v / self.u

    def test_unit_vector(self):
        self.assertEqual(self.v.unit(), self.v / self.v.magnitude())

    # uniary
    def test_pos_vector(self):
        self.assertEqual(+self.v, self.v)

    def test_neg_vector(self):
        self.assertEqual(-self.u, vectors.Vector(-2, -3, 0.5, -4, -3))

    # addition
    def test_add_vector_length(self):
        with self.assertRaises(vectors.VectorLengthError):
            self.v + vectors.Vector(1, 2, 3)

    def test_vector_add_vector(self):
        self.assertEqual(self.v + self.u,
                         vectors.Vector(6, -3, 6.5, 6.4, 13))

    def test_vector_add_tuple(self):
        self.assertEqual(self.v + (6, 6, 3, -2.4, 0),
                         vectors.Vector(10, 0, 10, 0, 10))

    def test_tuple_add_vector(self):
        self.assertEqual((6, 6, 3, -2.4, 0) + self.v,
                         vectors.Vector(10, 0, 10, 0, 10))

    def test_vector_add_list(self):
        self.assertEqual(self.u + [8, -3, 0.5, 6, 7],
                         vectors.Vector(10, 0, 0, 10, 10))

    def test_list_add_vector(self):
        self.assertEqual([8, -3, 0.5, 6, 7] + self.u,
                         vectors.Vector(10, 0, 0, 10, 10))

    # subtraction
    def test_sub_vector_length(self):
        with self.assertRaises(vectors.VectorLengthError):
            self.v - vectors.Vector(1, 2, 3)

    def test_vector_sub_vector(self):
        self.assertEqual(self.v - self.u,
                         vectors.Vector(2, -9, 7.5, -1.6, 7))

    def test_vector_sub_tuple(self):
        self.assertEqual(self.v - (4, 4, 7, -2.4, 0),
                         vectors.Vector(0, -10, 0, 4.8, 10))

    def test_tuple_sub_vector(self):
        self.assertEqual((4, 4, 7, -2.4, 0) - self.v,
                         vectors.Vector(0, 10, 0, -4.8, -10))

    def test_vector_sub_list(self):
        self.assertEqual(self.u - [2, -3, 0.5, 6, 7],
                         vectors.Vector(0, 6, -1, -2, -4))

    def test_list_sub_vector(self):
        self.assertEqual([2, -3, 0.5, 6, 7] - self.u,
                         vectors.Vector(0, -6, 1, 2, 4))

    def test_dimension(self):
        self.assertEqual(self.v.dimension(), 5)

class TestVector3(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.v = vectors.Vector3(1, 2, 3)
        self.u = vectors.Vector3(7, 4, 2)
        self.w = vectors.Vector3(2, 2*math.sqrt(3), 3)

    def tearDown(self):
        super().tearDown()

    # accessors
    def test_get_x(self):
        self.assertEqual(self.u.x, 7)

    def test_get_y(self):
        self.assertEqual(self.u.y, 4)

    def test_get_z(self):
        self.assertEqual(self.u.z, 2)

    # products
    def test_scalar_product_vector3_length(self):
        with self.assertRaises(vectors.VectorLengthError):
            vectors.Vector3.scalar_product(
                    self.v, vectors.Vector(5, 4, 3, 2, 1))

    def test_scalar_product_vector3_vector(self):
        self.assertEqual(vectors.Vector3.scalar_product(
            self.v, vectors.Vector(3, 2, 1)), 10)

    # vector product
    def test_vector_product(self):
        self.assertEqual(vectors.Vector3.vector_product(self.v, self.u),
                         vectors.Vector3(-8, 19, -10))

    def test_cross(self):
        self.assertEqual(vectors.Vector3.cross(self.v, self.u),
                         vectors.Vector3(-8, 19, -10))

    def test_vector_product_anticommutes(self):
        self.assertEqual(vectors.Vector3.vector_product(self.v, self.u),
                         -vectors.Vector3.vector_product(self.u, self.v))

    # addition
    def test_vector3_add_vector(self):
        self.assertEqual(self.u + vectors.Vector(3, 2, 1),
                         vectors.Vector3(10, 6, 3))

    # subtraction
    def test_vector3_sub_vector(self):
        self.assertEqual(self.u - vectors.Vector(3, 2, 1),
                         vectors.Vector3(4, 2, 1))

    # properties
    def test_spherical_polar_radius(self):
        self.assertEqual(self.w.r, 5)

    def test_azimuthal_angle(self):
        self.assertEqual(round(self.w.phi * 180/math.pi, 7), 60)

    def test_zenith_angle(self):
        self.assertEqual(math.cos(self.w.theta), 3/5)

    def test_cylindrical_polar_radius(self):
        self.assertEqual(self.w.rho, 4)

    def test_dimension(self):
        self.assertEqual(self.v.dimension(), 3)


class TestLorentzVector(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.v = vectors.LorentzVector(1, 2, 3, 4)
        self.u = vectors.LorentzVector(4, 3, 2, 1)

    def tearDown(self):
        super().tearDown()

    def test_covariant(self):
        self.assertEqual(vectors.LorentzVector._covariant(self.v),
                         vectors.LorentzVector(1, -2, -3, -4))

    def test_scalar_product(self):
        self.assertEqual(vectors.LorentzVector.scalar_product(
            self.v, self.u), -12)

    def test_spherical_polar_radius(self):
        self.assertEqual(self.u.r, math.sqrt(14))

if __name__ == '__main__':
    unittest.main()
