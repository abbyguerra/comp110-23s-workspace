"""Unit test functions."""

__author__ = "730556346"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens() -> None:
    """Edge case - testing with an empty list."""
    assert only_evens([]) == []
   
    """Use case 1 - testing even and odd numbers."""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    """Use case 2 - testing with only odd numbers."""
    assert only_evens([1, 3, 5, 7, 9, 11]) == []

def test_concat() -> None:
    """Edge case - testing with empty lists."""
    assert concat ([],[]) == []
    
    """Use case 1 - testing even and odd numbers."""
    assert concat ([1, 2, 3],[4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    
    """Use case 2 - testing with one empty list."""
    assert concat([1, 2, 3],[]) == [1, 2, 3]

def test_sub() -> None: 
    """Edge case - testing with an empty list."""
    assert sub([], 0, 0) == []
    
    """Use case 1 - testing with negative numbers."""
    assert sub([1, 2, 3], -1, 2) == [1, 2]
    
    """Use case 2 - testing a range of indices in the list."""
    assert sub([1, 2, 3, 4, 5, 6], 1, 5) == [2, 3, 4, 5]