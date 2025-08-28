"""Basic unit tests for all shape strategy classes.

These tests check that the area calculations for each shape work correctly.
Includes Circle, Rectangle, Triangle, and Square, and validates negative inputs.
"""

import unittest
from math import pi, isclose
from shapes.primitives.circle import Circle
from shapes.primitives.rectangle import Rectangle
from shapes.primitives.triangle import Triangle
from shapes.primitives.square import Square


class TestShapes(unittest.TestCase):
    """Test suite for area methods of all shape classes."""

    def test_circle_area_cases(self):
        """Check if Circle area is calculated correctly for simple cases."""
        circle1 = Circle(radius=1)
        circle2 = Circle(radius=3)

        self.assertTrue(isclose(circle1.area(), pi * 1**2))
        self.assertTrue(isclose(circle2.area(), pi * 3**2))

        # Negative value test
        with self.assertRaises(ValueError):
            Circle(radius=-5)

    def test_rectangle_area_cases(self):
        """Check if Rectangle area works as expected for a few sizes."""
        rect1 = Rectangle(width=2, height=3)
        rect2 = Rectangle(width=5, height=4)

        self.assertEqual(rect1.area(), 2 * 3)
        self.assertEqual(rect2.area(), 5 * 4)

        # Negative value test
        with self.assertRaises(ValueError):
            Rectangle(width=-2, height=3)

    def test_triangle_area_cases(self):
        """Check if Triangle area formula is correct for some examples."""
        tri1 = Triangle(base=4, height=3)
        tri2 = Triangle(base=10, height=5)

        self.assertEqual(tri1.area(), 0.5 * 4 * 3)
        self.assertEqual(tri2.area(), 0.5 * 10 * 5)

        # Negative value test
        with self.assertRaises(ValueError):
            Triangle(base=4, height=-3)

    def test_square_area_cases(self):
        """Check if Square area is calculated correctly for given sides."""
        sq1 = Square(side=2)
        sq2 = Square(side=5)

        self.assertEqual(sq1.area(), 2**2)
        self.assertEqual(sq2.area(), 5**2)

        # Negative value test
        with self.assertRaises(ValueError):
            Square(side=-4)


if __name__ == "__main__":
    unittest.main()
