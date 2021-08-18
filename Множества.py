numbers = {1, 2, 4, 6, 7, 89}
print(numbers)

numbers2 = set([1, 1, 1, 2, 3, 4, 5, 6, 54, 4, 2, 2, 34, 5, 4, 3, 3, 2, 4, 5])
print(numbers2)

for c in numbers:
    print(c)

print(3 in numbers)
print(3 in numbers2)

numbers.add(122)
print(numbers)

numbers.discard(58)
print(numbers)

numbers.remove(122)
print(numbers)

numbers.pop()
print(numbers)

numbers3 = numbers.union(numbers2)
print(numbers3)


numbers3 = numbers.intersection(numbers2)
print(numbers3)


numbers3 = numbers - numbers2
print(numbers3)

numbers3 = numbers2 - numbers
print(numbers3)

numbers3 = numbers2.copy()
print(len(numbers3))

numbers4 = frozenset({1,2,3,4,5,6,7,8,9})
print(numbers4)

numbers4.add(123)
print(numbers4)
