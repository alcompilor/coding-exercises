"""Square shape class that implements  the Shape abstraction."""

from shapes.shape import Shape
from shapes.mapping import map_shape


@map_shape("square")
class Square(Shape):
    """Square shape with a single side length."""

    def __init__(self, **args):
        """Construct square with a 'side' length."""
        side = args.get("side", 0)
        if side < 0:
            raise ValueError(f"Square side cannot be negative: {side}")
        self.side = side

    def area(self):
        """Return the area of the square."""
        return self.side**2
