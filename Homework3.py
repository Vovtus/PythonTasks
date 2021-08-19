# Создать список на 100 элементов, заполненный случайными числами.
# Поменять местами самый большой и самый маленький элементы списка.

import random

s = [random.randrange(100) for i in range(1, 10 + 1)]
print(s)

a = s.index(max(s))
b = s.index(min(s))
s[a], s[b] = s[b], s[a]

print(s)

q = input('Напишите 2 слова: ')
q = q.split()
q = q[1] + q[0]
print(q)
