"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730410140"


def test_only_evens() -> None:
    """Unit tests for list utility functions of even numbers."""
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]
    
    
def test2_only_evens() -> None:
    """Unit tests for list utility functions of even numbers."""
    xa: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xa) == []
    

def test3_only_evens() -> None:
    """Unit tests for list utility functions of even numbers."""
    xb: list[int] = [2, 2, 2]
    assert only_evens(xb) == [2, 2, 2]


def test1_sub() -> None:
    """Unit tests for list utility functions of selected numbers."""
    x: list[int] = [10, 20, 30, 40, 60]
    assert sub(x, 1, 7) == [20, 30, 40, 60]
    
   
def test2_sub() -> None:
    """Unit tests for list utility functions of selected numbers."""
    x: list[int] = [10, 20, 30, 40, 60]
    assert sub(x, 1, 4) == [20, 30, 40]


def test3_sub() -> None:
    """Unit tests for list utility functions of selected numbers."""
    x: list[int] = [10, 20, 30, 40, 60]
    assert sub(x, -1, 3) == [10, 20, 30]


def test_concat() -> None:
    """Unit tests for list utility functions of concatenation of two lists."""
    xa: list[int] = [1, 2]
    xb: list[int] = [4, 2, 3, 6]
    assert concat(xa, xb) == [1, 2, 4, 2, 3, 6]


def test2_concat() -> None:
    """Unit tests for list utility functions of concatenation of two lists."""
    xa: list[int] = [1, 2]
    xb: list[int] = [4, 2, 3, 6]
    assert concat(xb, xa) == [4, 2, 3, 6, 1, 2]
    

def test3_concat() -> None:
    """Unit tests for list utility functions of concatenation of two lists."""
    xb: list[int] = [4, 2, 3, 6]
    xx: list[int] = [3, 5, 7]
    assert concat(xx, xb) == [3, 5, 7, 4, 2, 3, 6]
