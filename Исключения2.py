try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except:
    print("Преобразование прошло неудачно")
print("Завершение программы")

#...

try:
    number2 = int(input("Введите число: "))
    print("Введенное число:", number2)
except ValueError:
    print("Не удалось преобразовать число")
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")

#...

try:
    number3 = int(input("Введите число: "))
    print("Введенное число:", number3)
except ValueError as e:
    print("Сведения об ошибке", e)
print("Завершение программы")

#...


