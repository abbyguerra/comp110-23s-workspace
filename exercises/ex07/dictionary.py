"""Dictionary functions."""

__author__ = "730556346"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverting the dictionary."""
    output: dict[str, str] = {}
    for x in dict1: 
        output[dict1[x]] = x
    if len(output) < len(dict1): 
        raise KeyError("Duplicate Keys!")
    return output


def favorite_color(dict2: dict[str, str]) -> str: 
    """Returning the most frequent color."""
    favorite: str = ""
    frequent: int = 0
    colors: dict[str, int] = {}
    for x in dict2.values(): 
        if x in colors: 
            colors[x] += 1
        else: 
            colors[x] = 1
    for y in colors:
        if colors[y] > frequent: 
            frequent = colors[y]
            favorite = [y]
    return favorite[0]


def count(lst: list[str]) -> dict[str, int]: 
    """Counting the items in the list."""
    result: dict[str, int] = {}
    for x in lst:
        if x in result: 
            result[x] += 1 
        else: 
            result[x] = 1
    return result 