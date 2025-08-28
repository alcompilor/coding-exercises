"""Circle shape class that implements  the Shape abstraction."""

import math
from shapes.shape import Shape
from shapes.mapping import map_shape


@map_shape("circle")
class Circle(Shape):
    """Circle shape with a radius."""

    def __init__(self, **args):
        """Construct circle with a 'radius',"""
        radius = args.get("radius", 0)
        if radius < 0:
            raise ValueError(f"Circle radius cannot be negative: {radius}")
        self.radius = radius

    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * (self.radius**2)
