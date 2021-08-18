import re

s = "32199sfdsdfsdfsdfsd>?>?<____-----     54534534  53435 889 e99 DFDFDFGhgjhgjhghj"
result = re.search(r"h.j", s)
print(result)

result = re.search(r"s..d", s)
print(result)

# Выводит любую цифру

result = re.search(r"\d", s)
print(result)

# Выводит несколько цифр
result = re.search(r"\d\d\d\d", s)
print(result)

# Выводит любой символ кроме цифры
result = re.search(r"\D", s)
print(result)

# Выводит люб пробельный символ
result = re.search(r"\s", s)
print(result)

# Выводит люб непробельный символ
result = re.search(r"\S", s)
print(result)

# Выводит любую букву, цифру, нижнее подчеркивание
result = re.search(r"\w", s)
print(result)

# Выводит любую не букву, не цифру, не нижнее подчеркивание (специальные знаки)
result = re.search(r"\W", s)
print(result)

# Начало слолва
result = re.search(r"\bDFD", s)
print(result)

# Не укажет границы слова
result = re.search(r"\BDFD", s)
print(result)

# Указывает 0 или более вхождений после символов после первой найденной цифры
result = re.search(r"\d*", s)
print(result)

# Указывает 1 или более вхождений после символов после первой найденной цифры
result = re.search(r"\d+", s)
print(result)

# Выведет результат если встретится одна из букв
result = re.search(r"[sdfg]", s)
print(result)

# Выведет результат если встретится одна из цифр
result = re.search(r"[4-8]", s)
print(result)

# Выведет то, что не входит в заданный диапазон
result = re.search(r"[^4-8]", s)
print(result)

# Высти дибо одну, либо другую
result = re.search(r"g|F", s)
print(result)

# Выведет результат если встретится одна из цифр
result = re.search(r"[4-8]", s)
print(result)

s2 = "Привет! Как дела? А у меня нормально!"
result = re.findall(r'[цкнгшщзхфвпрлджчсмтбЦКНГШЩЗХФВПРЛДЖЧСМТБ]\w+', s2)
print(result)
