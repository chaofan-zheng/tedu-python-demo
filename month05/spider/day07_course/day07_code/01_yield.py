def f1():
    for i in range(2):
        yield i

g = f1()
print(next(g))
print(next(g))
