"""Dict function writing."""

__author__ = "730556346"

from typing import Dict, List 

def zip(strings: 'list[str]', ints: 'list[int]') -> Dict[str, int]:
    if len(strings) != len(ints): 
        return()
    result = []
    for i in range(len(strings)):
        result [strings[i]] = ints[i]
    return result 

