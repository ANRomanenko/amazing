# Калькулятор

number = input("Введите что бы выхотели посчитать: (+, -, *, /)? ")

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

if number == '+':
    print(a + b)
elif number == '-':
    print(a - b)
elif number == '*':
    print(a * b)