"""Triangle shape class that implements  the Shape abstraction."""

from shapes.shape import Shape
from shapes.mapping import map_shape


@map_shape("triangle")
class Triangle(Shape):
    """Triangle shape with base and height."""

    def __init__(self, **args):
        """Construct triangle with 'base' and 'height'."""
        base = args.get("base", 0)
        height = args.get("height", 0)

        if base < 0:
            raise ValueError(f"Triangle base cannot be negative: {base}")
        if height < 0:
            raise ValueError(f"Trangle height cannot be negative: {height}")

        self.base = base
        self.height = height

    def area(self):
        """Return the area of the triangle."""
        return (self.height * self.base) / 2
