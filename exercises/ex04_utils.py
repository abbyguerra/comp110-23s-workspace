"""List utility functions."""
__author__ = "730556346"

def all(list0: "list[int]", item: int) -> bool:
    if list0 == list(): 
        return False
    index: int = 0
    while index < len(list0): 
        if item != list0[index]: 
            return False
        else: 
            index = index + 1
    return True 

def max(input: "list[int]") -> int: 
    """Find the max value int"""
    high_value = input[0]
    index: int = 0
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    while index < len(input): 
        if input[index] > high_value: 
            high_value = input[index]
            index = index + 1
        else: 
            index = index + 1 
    return high_value 

def is_equal(list1: "list[int]", list2: "list[int]"): 
    """See if both lists are equal"""
    if len(list1) != len(list2): 
        return False 
    index: int = 0 
    while index < len(list1): 
        if list1[index] != list2[index]:
            return False 
        else: 
            index = index + 1
    return True 
    



    

