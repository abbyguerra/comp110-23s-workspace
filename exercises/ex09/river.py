"""Importing the necessary classes."""
from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


"""File to define River class."""

__author__ = "730556346"


class River:
    """Defining the river class."""  
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def bears_eating(self): 
        """What happens when a bear eats the fish."""
        for bear in self.bears: 
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)
    
    def check_hunger(self):
        """Removing starving bears from the river."""
        new_bears = []
        for bear in self.bears: 
            if bear.hunger_score < 0: 
                continue 
            new_bears.append(bear)
        self.bears = new_bears 
        
    def repopulate_fish(self):
        """Each pair of fish produces four offspring."""
        num_pairs = len(self.fish) // 2
        for _ in range(num_pairs): 
            for _ in range(4): 
                self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Each pair of bears produces one offspring."""
        num_pairs = len(self.bears) // 2
        for _ in range(num_pairs): 
            self.bears.append(Bear())
    
    def view_river(self):
        """Printing the river status.""" 
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        
    def one_river_week(self): 
        """Simulate one  week in the life in the river."""
        for i in range(7): 
            self.one_river_day()

    def check_ages(self):
        """Checking the age of the bears and fish."""
        new_fish = []
        new_bears = []
        for fish in self.fish: 
            if fish.age > 3: 
                continue
            new_fish.append(fish)
        self.fish = new_fish 
        for bear in self.bears: 
            if bear.age > 5: 
                continue
            new_bears.append(bear)
        self.bears = new_bears
    
    def remove_fish(self, amount: int) -> None: 
        """Removing fish from the river."""
        if len(self.fish) < amount:
            raise ValueError("There are not enough fish in the river.")
        for i in range(amount): 
            self.fish.pop(0)
        


            
