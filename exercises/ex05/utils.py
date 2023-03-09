"""List utility functions."""

__author__ = "730556346"


def only_evens(input: 'list(int)') -> int:
    """Listing only even numbers."""
    even_list = []
    for num in input: 
        if num % 2 == 0:
            even_list.append(num)
    return even_list 


def concat(list1: 'list(int)', list2: 'list(int)') -> int:
    """Combining two lists."""
    new_list = []
    for num in list1: 
        new_list.append(num)
    for num in list2: 
        new_list.append(num)
    return new_list


def sub(list: 'list(int)', start: int, end: int) -> 'list(int)':
    """Making a subset of a list."""
    if len(list) == 0 or start >= len(list) or end <= 0: 
        return []
    if start < 0:
        start = 0 
    if end > len(list): 
        end = len(list)
    return list[start:end]