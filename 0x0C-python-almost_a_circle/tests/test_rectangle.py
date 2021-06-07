#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectCls(unittest.TestCase):
    def test_init(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10)
        y = Rectangle(10, 10)
        self.assertEqual(x.id, 1)
        self.assertEqual(y.id, 2)

    def test_attrs(self):
        Base._Base__nb_objects = 0
        x = Rectangle(10, 10, 10, 10, 15)
        self.assertEqual(x.width, 10)
        self.assertEqual(x.height, 10)
        self.assertEqual(x.x, 10)
        self.assertEqual(x.y, 10)
        self.assertEqual(x.id, 15)
        
    def test_attrs_validation(self):
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            y = Rectangle("20", 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            y = Rectangle(20, "20")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            y = Rectangle(20, 20, "x", 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            y = Rectangle(20, 20, 10, "y")

if __name__ == "__main__":
    unittest.main()