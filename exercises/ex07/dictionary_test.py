"""Testing the dictionary functions."""

__author__ = "730556346"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Edge case: testing with duplicate values."""
    try:
        invert({'amy': 'steve', 'katie': 'steve'}) 
        assert False, "Exception not raised!"
    except KeyError as x: 
        assert str(x) == "Duplicate Keys!"


def test_invert_1() -> None:
    """Use case: testing with unique str."""
    assert invert({'cat': 'dog'}) == {'dog': 'cat'}


def test_invert_2() -> None:
    """Use case: testing with unique str."""
    assert invert({'a': 'b', 'c': 'd'}) == {'b': 'a', 'd': 'c'}


def test_favorite_color() -> None:
    """Edge case: testing with unique values."""
    assert favorite_color({'Marc': 'red', 'John': 'blue', 'Alisha': 'orange'}) == 'red'


def test_favorite_color_1() -> None: 
    """Use case: testing with tied frequencies."""
    assert favorite_color({'Marc': 'yellow', 'John': 'blue', 'Billy': 'blue', 'Jack': 'yellow'}) == 'yellow'


def test_favorite_color_2() -> None:
    """Use case: testing with one favorite color."""
    assert favorite_color({'Alexa': 'pink', 'Abby': 'pink', 'Amy': 'pink'}) == 'pink'


def test_count() -> None:
    """Edge case: testing with an empty list."""
    assert count([]) == {}


def test_count_1() -> None: 
    """Use case: testing with duplicates."""
    assert count(['cat', 'dog', 'bunny', 'dog']) == {'cat': 1, 'dog': 2, 'bunny': 1}


def test_count_2() -> None:
    """Use case: testing with unique items."""
    assert count(['red', 'orange', 'yellow']) == {'red': 1, 'orange': 1, 'yellow': 1}