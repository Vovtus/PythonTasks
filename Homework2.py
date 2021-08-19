# Дан список из 100 элементов, заполненный случайными числами.
# Найти и вывести все элементы списка, которые больше своих соседей.

from random import randint

s = [randint(1, 100) for i in range(10)]
print(s)
for i in range(1, len(s)-1):
    if s[i]> s[i+1] and s[i] > s[i-1]:
        print(s[i])
