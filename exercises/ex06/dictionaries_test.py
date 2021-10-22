"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730410140"

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert() -> None:
    """Unit tests for list utility functions of invert."""
    xs: dict[str, str] = {"Jim": "Appiah", "Sammy": "Adjei", "Osei": "Asamoah"}
    assert invert(xs) == {"Appiah": "Jim", "Adjei": "Sammy", "Asamoah": "Osei"}
    
    
def test2_invert() -> None:
    """Unit tests for list utility functions of invert."""
    xa: dict[str, str] = {"Jim": "Appiah", "Sammy": "Adjei", "Osei": "Agyei"}
    assert invert(xa) == {"Appiah": "Jim", "Adjei": "Sammy", "Agyei": "Osei"}
    

def test3_invert() -> None:
    """Unit tests for list utility functions of invert."""
    xb: dict[str, str] = {"a": "y", "b": "x", "c": "z"}
    assert invert(xb) == {"y": "a", "x": "b", "z": "c"}


def test1_favorite_color() -> None:
    """Unit tests for list utility functions of favorite color."""
    x: dict[str, str] = {"c1": "red", "c2": "red", "c3": "yellow"}
    assert favorite_color(x) == "red"

     
def test2_favorite_color() -> None:
    """Unit tests for list utility functions of favorite color."""
    x: dict[str, str] = {"c1": "red", "c2": "yellow", "c3": "red", "c4": "yellow"}
    assert favorite_color(x) == "red"


def test3_favorite_color() -> None:
    """Unit tests for list utility functions of favorite color."""
    xa: dict[str, str] = {"c1": "red", "c2": "yellow"}
    assert favorite_color(xa) == "red"


def test1_count() -> None:
    """Unit tests for list utility functions of count."""
    x: list[str] = ["red", "yellow", "red", "blue"]
    assert count(x) == {"red": 2, "yellow": 1, "blue": 1}


def test2_count() -> None:
    """Unit tests for list utility functions of count."""
    xa: list[str] = ["red", "yellow", "blue"]
    assert count(xa) == {"red": 1, "yellow": 1, "blue": 1}


def test3_count() -> None:
    """Unit tests for list utility functions of count."""
    xa: list[str] = ["red", "yellow", "blue", "pink"]
    assert count(xa) == {"red": 1, "yellow": 1, "blue": 1, "pink": 1}
