"""Dictionary functions."""

__author__ = "730556346"


def invert(dict1: 'dict[str, str]') -> 'dict[str, str]': 
    """Inverting the dictionary."""
    output: dict[str, str] = {}
    for x in dict1:
        if [dict1[x]] in output:
            raise ValueError("Duplicate Keys!")
        output[dict1[x]] = x
    return output


def favorite_color(dict2: 'dict[str, str]') -> str: 
    """Returning the most frequent color."""
    favorite: str = []
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
            favorite = {}
    return favorite 


def count(list1: 'list[str]') -> 'dict[str, int]': 
    """Counting the items in the list."""
    result: dict[str, int] = {}
    for x in list1:
        if x in result: 
            result[x] += 1 
        else: 
            result[x] = 1
    return result 