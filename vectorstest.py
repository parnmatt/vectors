#!/usr/bin/env python3

import unittest
import vectors

class TestVectors(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.v = vectors.Vector(1, 2, 3)

    def tearDown(self):
        super().tearDown()

    def test_init(self):
        self.assertEqual(self.v.x, 1)
        self.assertEqual(self.v.y, 2)
        self.assertEqual(self.v.z, 3)


if __name__ == '__main__':
    unittest.main()