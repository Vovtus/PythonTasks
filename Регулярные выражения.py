import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DC/AC/ACDC/ACDC/DC/AC/DC'

# Ищет в начале строки match
result = re.match('AC', s)
print(result)
result = re.match('DC', s)
print(result)
result = re.match('ac', s)
print(result)

#search Определяет где находится первое совпадение
result =re.search('DC', s)
print(result)

#findall Ищет все совпадения
result =re.findall('DC', s)
print(result)

#split Разделяет строчку по заданному шаблону

result =re.split('/', s)
print(result)

#sub Меняет одну подстроку на другую

result =re.sub('A','D', s)
print(result)

#fullmatch Проверяет подхлдит ли всё регулярное выражение под заданную строчку

result =re.fullmatch('A', s)
print(result)

s2='A'
result =re.fullmatch('A', s2)
print(result)

s3='AAAA'
result =re.fullmatch('A', s3)
print(result)