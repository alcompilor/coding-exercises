"""Mapping and decorator to map shape names to their classes."""

SHAPE_MAPPINGS = {}


def map_shape(name: str):
    """Decorator to register a shape class under a given name."""

    def decorator(cls):
        SHAPE_MAPPINGS[name.lower()] = cls
        return cls

    return decorator
