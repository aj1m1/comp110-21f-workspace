"""Finding duplicate letters in a word."""

__author__ = "730410140"

user_word: str = input('Enter a word: ')
dup: bool = False

i: int = 0
while i < len(user_word):
    charater = user_word[i]
    j: int = i + 1
    while j < len(user_word):
        if user_word[j] == user_word[i]:
            dup = True
        j = j + 1
    i = i + 1
print("Found duplicate: " + str(dup))