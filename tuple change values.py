x = ("apple","mango","banana")
y = list(x)
y[1] = "orange"
x = tuple(y)

print(x)