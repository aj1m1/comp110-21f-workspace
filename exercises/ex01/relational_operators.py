"""A program to practice relational_operators """

__author__ = "730410140"

First_number: int = int(input("Choose a number: "))
second_number: int = int(input("Choose another number: "))
print(str(First_number) + "<" + str(second_number) + "is" + str(First_number < second_number))
print(str(First_number) + ">=" + str(second_number) + "is" + str(First_number <= second_number)) 
print(str(First_number) + "==" + str(second_number) + "is" + str(First_number == second_number)) 
print(str(First_number) + "!=" + str(second_number) + "is" + str(First_number != second_number)) 