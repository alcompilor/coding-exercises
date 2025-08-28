"""Aggregator class to load shapes, calculate total area, and save results."""

from utils.io import IOService


class ShapeAggregator:
    """Handles shapes: loading, calculating total area, and saving."""

    def __init__(self, io_service: IOService, shape_mappings: dict):
        """Construct with I/O service and shape mappings."""
        self.io = io_service
        self.shape_map = shape_mappings

        self.shapes = []
        self.shape_counts = {}

    def load_shapes(self, file_path: str) -> None:
        """Load shapes from a JSON file and define shape instances."""
        data = self.io.read_from_json(file_path)
        for entry in data:
            shape_class = self.shape_map.get(entry["type"].lower())

            if shape_class:
                self.shapes.append(shape_class(**entry))
                self.shape_counts[entry["type"]] = (
                    self.shape_counts.get(entry["type"], 0) + 1
                )

            else:
                print(
                    f"Ignored unknown shape '{entry['type']}'. "
                    f"Supported shapes: {list(self.shape_map.keys())}"
                )

    def get_total_area(self, precision: int = 1) -> float:
        """Return the total area of all loaded shapes."""
        return round(sum(shape.area() for shape in self.shapes), precision)

    def save_total_area(self, output_path: str) -> None:
        """Save the total area of all loaded shapes to a text file."""
        self.io.save_to_txt(
            f"Total Area: {self.get_total_area()} square units", output_path
        )

    def get_shape_counts(self) -> dict:
        """Return a dictionary with the number of each shape loaded."""
        return self.shape_counts
