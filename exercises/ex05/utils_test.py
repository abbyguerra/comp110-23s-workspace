"""Unit test functions."""

__author__ = "730556346"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_blank() -> None:
    """Edge case - testing with an empty list."""
    assert only_evens([]) == []


def test_only_evens_even_odd() -> None:
    """Use case 1 - testing even and odd numbers."""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_only_evens_odd() -> None:
    """Use case 2 - testing with only odd numbers."""
    assert only_evens([1, 3, 5, 7, 9, 11]) == []


def test_concat_blank() -> None:
    """Edge case - testing with empty lists."""
    assert concat([], []) == []


def test_concat_even_odd() -> None:
    """Use case 1 - testing even and odd numbers."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_empty() -> None: 
    """Use case 2 - testing with one empty list."""
    assert concat([1, 2, 3], []) == [1, 2, 3]


def test_sub_blank() -> None: 
    """Edge case - testing with an empty list."""
    assert sub([], 0, 0) == []


def test_sub_negative() -> None:
    """Use case 1 - testing with negative numbers."""
    assert sub([1, 2, 3], -1, 2) == [1, 2]

    
def test_sub_range() -> None:
    """Use case 2 - testing a range of indices in the list."""
    assert sub([1, 2, 3, 4, 5, 6], 1, 5) == [2, 3, 4, 5]