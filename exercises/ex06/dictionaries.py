"""Practice with dictionaries."""

__author__ = "730410140"

# # Define your functions below


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Return a reversed dict, with strings switched."""
    dic = {}
    for i in xs:
        if xs[i] in dic:
            raise KeyError('KeyError')
        else:
            if xs[i] not in dic:
                dic[xs[i]] = i
    return(dic)

    
def favorite_color(xs: dict[str, str]) -> str:
    """From a given list of colors return the color that appears most."""
    dic = {}
    values = xs.values()
    for i in values:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    val = list(dic.values())
    key = list(dic.keys())
    x: str = ''
    maximum = max(val)
    for i in range(len(val)):
        if val[i] == maximum:
            return key[i]
    return x


def count(s: list[str]) -> dict[str, int]:
    """From  a list return the number and string."""
    xs = {}
    for i in s:
        if i not in xs:
            xs[i] = 1
        else:
            xs[i] += 1

    return xs


xs = ['blue', 'red', 'blue', "indigo", 'pink', 'green', 'blue']
print(count(xs))
xs = {'kris': 'jorda', 'mich': 'john'}
print(invert(xs))
xs = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Jim": "yellow"}
print(favorite_color(xs))