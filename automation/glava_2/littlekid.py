name = 'Alice'
age = 14

if name == 'Alice':
    print('Hi, Alice')
    if age > 12:
        print('Внутри блока, код выполнился также')
else:
    print('You are neither Alice nor a little kid.')
print()

name_1 = input("Введите любое имя: ")
age = input("Ведите возраст: ")

if name_1 == name_1:
    print(f"Hi, {name_1}")
    if int(age) > 12:
        print("Эта строка выполниться также!")
else:
    print("Все выше действия не верны!")