def f(a):
    if a % 2 == 0:
        return a


a = filter(f, (2, 4, 5))
print(list(a))

a2 = filter(lambda x: (x % 2 == 0), (2, 4, 5))
print(list(a2))