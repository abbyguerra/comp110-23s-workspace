"""Defining the Bear class."""

__author__: 730556346


class Bear:
    """A class representing the bears living in the river."""
    def __init__(self):
        """Initializing age and hunger score to 0."""
        self.age = 0 
        self.hunger_score = 0

    def one_day(self):
        """Changing age and hunger score after one day."""
        self.age += 1 
        self.hunger_score -= 1
        
    def eat(self, num_fish: int) -> None: 
        """Adding fish to hunger score each time it eats."""
        self.hunger_score += num_fish 

    