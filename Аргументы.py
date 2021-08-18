def summa(a, b, c):
    print(a + b + c)


summa(1, 2, 3)


def summa2(a, b=7, c=8):
    print(a + b + c)


summa2(1, 2)


def summa3(a, b=7, c=8):
    print(a + b + c)


summa3(1, 70, 80)


def summa4(a, b=7, c=8):
    print(a, b, c)


summa4(c=1, b=80, a=70)


def summa5(*args):
    print(args)


summa5(7, 8, 9, 1, 10)


def summa6(*numbers):
    print(sum(numbers))


summa6(7, 8, 9, 1, 10)


def brand(**brands):
    print(brands)


brand(a='Apple', s='Samsung')


def brand2(**brands2):
    for x, y in brands2.items():
        print(x, ':', y)


brand2(a='Apple', s='Samsung')
