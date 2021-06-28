import unittest
import pytest
from modulus_zero import ModulusZero


class Modulustest(unittest.TestCase):
    mod = ModulusZero()

    def test_divisable(self):
        self.assertEqual(self.mod.divisable(12, 3), True)

    def test_modulus(self):
        self.assertEqual(self.mod.modulus(11, 3), 2)

    def test_positive(self):
        self.assertEqual(self.mod.positive(12, 2), True)
