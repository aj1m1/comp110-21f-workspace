"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730410140"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune_number: int = randint(1, 4)
print("Your fortune cookie says...")
if fortune_number == 4:
    print("You Have amazing professors and TA's who will ensure your success.")
else:
    if fortune_number == 3:
     print("A lot of great opportunities are coming your way, don't be scared to make sacrifices.")
    else:
        if fortune_number == 2:
         print("Stay focused cos your are a victor.")
        else:
         print("You will buy a car this year.")

print("Now go and spread positive vibes!")




