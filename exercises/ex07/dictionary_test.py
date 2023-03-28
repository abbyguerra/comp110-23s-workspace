"""Testing the dictionary functions."""

__author__ = "730556346"

def test_invert() -> None:
    """Edge case: testing with an empty dict."""
    assert invert[()] == []


def test_invert() -> None:
    """Use case: inverting str in a list."""
    assert invert[('apple': 'cat')] == ['cat': 'apple']


def test_invert() -> None:
    """Use case: inverting str in a dict using chr."""
    assert invert[('a': 'b', 'c': 'd')] == ['b': 'a', 'd': 'c']


def test_favorite_color() -> None:
    """Edge case: testing with an empty dict"""
    assert favorite_color[()] == []


def test_favorite_color() -> None:
    """Use case: printing the most popular color."""
    assert favorite_color[('Marc': 'yellow', 'John': 'blue', 'Billy': 'blue')] == ['blue']


def test_favorite_color() -> None:
    """Use case: """
    assert favorite_color[()] == []


def test_count() -> None: 
    """Edge case: """
    assert count[()] == []


def test_count() -> None: 
    """Use case: """
    assert count[()] == []


def test_count() -> None: 
    """Use case: """
    assert count[()] == []

