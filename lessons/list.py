a: list[str] = ["one"]
b: list[str] = a
a.append("two")
b.append("?")

print(b[2])