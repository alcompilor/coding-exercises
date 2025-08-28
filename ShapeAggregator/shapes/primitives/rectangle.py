"""Rectangle shape class that implements  the Shape abstraction."""

from shapes.shape import Shape
from shapes.mapping import map_shape


@map_shape("rectangle")
class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, **args):
        """Construct rectangle with 'width' and 'height'."""
        width = args.get("width", 0)
        height = args.get("height", 0)

        if width < 0:
            raise ValueError(f"Rectangle width cannot be negative: {width}")
        if height < 0:
            raise ValueError(f"Rectangle height cannot be negative: {height}")

        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height
