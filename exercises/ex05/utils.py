"""List utility functions."""

__author__ = "730556346"

def only_evens(input: 'list[int]') -> list(int): 
    """Listing only even numbers."""
    even_list = ""
    for num in input: 
        if num % 2 == 0:
            even_list.append(num)
    return even_list 

def concat(list1: 'list[int]', list2: 'list[int]') -> list(int): 
    """"""
    new_list = ""
    for num in list1: 
        new_list.append(num)
    for num in list2: 
        new_list.append(num)
    return new_list

def sub(list:'list[int]',start: int, end: int) -> list(int):
    """"""
    return list[start:end]