#!/usr/bin/python3
import unittest
from models.base import Base


class TestBaseCls(unittest.TestCase):
    def test_cls(self):
        b1 = Base()
        b2 = Base()
        b12 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b12.id, 12)
        self.assertEqual(b3.id, 3)

if __name__ == "__main_":
    unittest.main()
