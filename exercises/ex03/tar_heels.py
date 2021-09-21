"""An exercise in remainders and boolean logic."""

__author__ = "730410140"

number: int = int(input("Enter an integer: "))
mod = number % 2
mod_two = number % 7


if mod == 0 and mod_two == 0:
    print("TAR HEELS")

else:
    if mod == 0:
        print("TAR")
    else:
        if mod_two == 0:
            print("HEELS")
        else:
            print("CAROLINA")