with open('69.TXT') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(int, f.readline().split())
        print(a, b)


def f(a, b):
    return a * b


a = map(f, [2, 4, 5, ], [5, 6, 7])
print(list(a))


a = map(lambda x: x+15, (2, 4, 5))
print(list(a))
