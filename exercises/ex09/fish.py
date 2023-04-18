"""Defining the Fish class."""

__author__: 730556346


class Fish:
    """A class representing the fish living in the river."""
    def __init__(self):
        """Initializing age to 0."""
        self.age = 0
    
    def one_day(self):
        """Changing age after one day."""
        self.age += 1