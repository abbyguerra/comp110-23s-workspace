"""Unit test functions."""

__author__ = "730556346"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens() -> None:
    """Edge case."""
    assert only_evens[()] == []

    """Use case 1."""
    assert only_evens[(1,2,3,4,5,6)] == [2,4,6]

    """Use case 2."""
    assert only_evens[(1,3,5,7,9,11)] == []

def test_concat() -> None:
    """Edge case."""
    assert concat[(),()] == []
    
    """Use case 1."""
    assert concat[(1,2,3),(4,5,6)] == [1,2,3,4,5,6]

    """Use case 2."""
    assert concat[(1,2,3),()] == [1,2,3]

def test_sub() -> None: 
    """Edge case."""
    assert sub[(),0,0] == []
    
    """Use case 1."""
    assert sub[(1,2,3),-1,2,3] == [1,2]

    """Use case 2."""
    assert sub[(1,2,3,4,5,6),1,4,6] == [2,3,4,6]