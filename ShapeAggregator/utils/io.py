"""I/O utility class."""

import json


class IOService:
    """Simple I/O service to read JSON and save text."""

    def __init__(self):
        pass

    def read_from_json(self, path: str):
        """Read JSON file and return its content."""
        with open(path, mode="r", encoding="utf-8") as file:
            return json.load(file)

    def save_to_txt(self, data: str, output_file: str):
        """Append a string to a text file."""
        with open(output_file, mode="a", encoding="utf-8") as file:
            file.write(f"{data}\n")
