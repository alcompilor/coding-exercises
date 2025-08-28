"""Base abstract class for shapes with common methods like area and perimeter."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class for all shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
