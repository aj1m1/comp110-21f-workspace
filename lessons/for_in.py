"""An example of for in syntax."""

names: list[str] = ["Jim", "Appiah", "Osei"]

#example of iterating through names using a while loop 
i: int = 0
print("While output")
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

#The following for...in loop is the same as the while loop
print("for...in")
for name in names:
    print(name)