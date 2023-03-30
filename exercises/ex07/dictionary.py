"""Dictionary functions."""

__author__ = "730556346"


def invert(dict1: 'dict[str, str]') -> 'dict[str, str]': 
    """Inverting the dictionary."""
    output: dict[str, str] = {}
    for x in dict1:
        if dict1[x] in output.values():
            raise ValueError("Duplicate Values!")
        if dict1[x] in output.key():
            raise ValueError("Duplicate Keys!")
        output[dict1[x]] = x
    return output


def favorite_color(dict2: 'dict[str, str]') -> 'list[str]': 
    """Returning the most frequent color."""
    favorite: list[str] = []
    frequent: int = 0
    colors: dict[str, int] = {}
    for x in dict2.values(): 
        if x in colors: 
            colors[x] += 1
        else: 
            colors[x] = 1
        if colors[x] > frequent: 
            frequent = colors[x]
            favorite = [x]
        elif colors[x] == frequent:
            favorite.append(x)
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