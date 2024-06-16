name = 'Mary'
password = 'swordfish'


if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password')
else:
    print('User not registered')

print()

name = 'Alices'

if name == 'Alice':
    print('Hi, Alice')

else:
    print('Hello, stranger')

print()

# elif

name = input('Введите имя ребёнка: ')

age = int(input("Введите возраст ребёнка: "))

if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo.')

else:
    print('Условие не выполнено')