"""List utility functions part 2."""


__author__ = "730410140"
# Define your functions below


def only_evens(integer_list: list[int]) -> list[int]:
    """From a given list of numbers, return the even numberss as list."""
    i: int = 0
    even_numbers_list: list[int] = []
    while i < len(integer_list):
        trial_numbers: int = integer_list[i]
        if trial_numbers % 2 == 0:
            even_numbers_list.append(trial_numbers)
        i += 1
    return even_numbers_list


def sub(x: list[int], start_index: int, end_index_not_inclusive: int) -> list[int]:
    """From a given list of numbers, return a subset of index 1 and end index -1 exclusive."""
    what_user_want: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index_not_inclusive > len(x):
        end_index_not_inclusive = len(x)
    if len(x) == 0 or end_index_not_inclusive <= 0:
        return what_user_want
    while start_index < end_index_not_inclusive:
        
        what_user_want.append(x[start_index])
        start_index += 1
    return what_user_want


def concat(x: list[int], y: list[int]) -> list[int]:
    """Given two lists, concatenate the two lists."""
    new_list: list[int] = x + y
    return new_list


given_list: list[int] = [1, 8, 3]
given_list2: list[int] = [2, 3, 5]
print(only_evens(given_list))
a_list = [1, 2, 3, 4]
print(concat(given_list, given_list2))

print(sub(a_list, 1, 0))