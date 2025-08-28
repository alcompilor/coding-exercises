"""Main module for the Shape Aggregator project.

This script allows the user to calculate the total area of different shapes
from a JSON file and save the result to a text file. Can be run from CLI.
"""

import argparse
import os

from aggregator.shape_aggregator import ShapeAggregator
from shapes.mapping import SHAPE_MAPPINGS
from utils.io import IOService


def main() -> None:
    """Start the Shape Aggregator CLI.

    It loads shapes from a JSON file, calculates their total area,
    prints it, and saves it to a file.

    Command line arguments:
        --file: (optional), path to the JSON file with shapes.
        --output: (optional), path to save the total area.

    Args default to 'shapes.json' and 'area.txt' in the current directory.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    default_json = os.path.join(base_path, "shapes.json")
    default_output = os.path.join(base_path, "area.txt")

    parser = argparse.ArgumentParser(description="Calculate total area of shapes.")
    parser.add_argument(
        "--file",
        type=str,
        help="Path to JSON file with shapes",
        default=default_json,
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path to save the total area",
        default=default_output,
    )
    args = parser.parse_args()

    # Setup services and aggregator
    io_service = IOService()
    aggregator = ShapeAggregator(io_service=io_service, shape_mappings=SHAPE_MAPPINGS)

    aggregator.load_shapes(args.file)
    total_area = aggregator.get_total_area()
    shape_count = aggregator.get_shape_counts()
    aggregator.save_total_area(args.output)

    # Output total area
    print(f"\nTotal area: {total_area} square")

    print("\nShape counts:")
    for shape, count in shape_count.items():
        print(f"\t{shape}: {count}")


if __name__ == "__main__":
    main()
