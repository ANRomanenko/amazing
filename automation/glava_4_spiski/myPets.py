# Операторы in и not in
# while True:
#     myPets = ['Zophie', 'Pooka', 'Fat-tail']
#     name = input('Enter a pet name:\n')
#     if name not in myPets:
#         print('I do not have a pet named: ' + name + "\n")
#     else:
#         print(name + ' is my pet.')
#         break

# print()

# Трюк с групповым присваиванием
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(disposition)
print()

# Можно ограничится следующий кодом
cat = ['fat', 'black', 'loud']

size, color, disposition = cat
print(size)
print()

# Комбинированные операторы присваивания
spam = 42
spam = spam + 1
print(spam)

spam = 42
spam += 1
print(spam)
print()

spam = 'Hello'
spam += ' world!'
print(spam)
print()

bacon = ['Zophie']
bacon *= 3
print(bacon)

print(cat.index('black'))
print()

# Поиск значения в списке с помощью метода index()
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))
# print(spam.index('howdy howdy howdy')) # Указанное значение отсутствует в списке, ошибка!
print()

# Наличие в списке дубликатов данного значение возвращается индекс первого из элементов!
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))
print()

# Добавления значений в список с помощью методов append() и insert()
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)
print()

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)