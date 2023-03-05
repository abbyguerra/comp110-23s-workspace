"""Example function for unit tests."""

def sum (xs: 'list[float]') -> float: 
    """return sum of all elements in xs."""
    sum: int = 0
    for elem in range(0,len(xs)):
        sum = sum + xs[elem]
    return sum 