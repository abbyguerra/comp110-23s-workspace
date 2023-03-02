"""Example function for unit tests."""

def sum(xs:"list[float]") -> float: 
    """return sum of all elements in xs"""
    sum: int = 0
    for elem in xs: 
        sum = sum + elem 
    return sum
    
