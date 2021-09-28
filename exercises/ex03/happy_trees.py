"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
if depth <= 0:
    print("")
Tree: str = ""
while depth > 0:
    Tree = Tree + TREE

    depth = depth - 1
    print(Tree)