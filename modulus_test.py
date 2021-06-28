import unittest
import pytest
from modulus_zero import ModulusZero


class Modulustest(unittest.TestCase):
    mod = ModulusZero()

    def test_modulus(self):
        self.assertEqual(self.mod.modulus(12, 3), 0)
