"""List utility functions."""

__author__ = "730410140"


def main() -> None:
    """Procedure for program."""
    integers_list: list[int] = [1, 1, 1]
    chosen_number: int = 9
    user_list: list[int] = [1, 1, 1, 1]
    print(all(integers_list, chosen_number))
    print(is_equal(integers_list, user_list))
    print(max(user_list))


def all(x: list[int], y: int) -> bool:
    """Return  True indicating if the ints in the list are the same as the given."""
    i: int = 0
    Length: int = len(x)
    if Length == 0:
        return False
    while i < Length:
        if x[i] != y:
            return False
        i += 1
    return True


def max(integer_list: list[int]) -> int:
    """Get maximum value from list."""
    i: int = 0
    maximum_number: int = integer_list[i]
    while i < len(integer_list) - 1:
        if maximum_number < integer_list[i + 1]:
            maximum_number = integer_list[i + 1]
        i = i + 1
    return maximum_number
    

def is_equal(integer_list: list[int], user_list: list[int]) -> bool:
    """Return  True indicating if the ints in the list are the same as the given list."""
    i: int = 0
    length: int
    length1: int = len(integer_list)
    length2: int = len(user_list)
    if length1 != length2:
        return False
    else: 
        length = length2
        if length == 0:
            return True
    while i < length - 1:
        if integer_list[i] != user_list[i]:
            return False
        i += 1
    return True


if __name__ == "__main__":
    main()