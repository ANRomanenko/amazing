list_1 = [1, 2, 3]
print(list_1[2])

list_2 = ['cat', 'bat', 'rat', 'elephant']
print(list_2[3])

list_3 = ['hello', 3.1415, True, None, 42]
print(list_3[2])

spam = ['cat', 'bat', 'rat']
print('Hello ' + spam[0])

list_card = []

# spam = ['cat,', 'bat', 'rat'] # выводит ошибку так как такого индекса не существует
# print(spam[1000])

spam = ['cat', 'bat', 'rat']
print(spam[1])
# print(spam[1.0]) # индексы могут принимать только целочисленные значения (не вещественные) пример 1.0

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1]) # элементы списков сами могут быть списками, доступ к таким спискам осуществляется с помощью нескольких индексов spam[0][1]
print(spam[1][4]) # элементы списков сами могут быть списками, доступ к таким спискам осуществляется с помощью нескольких индексов spam[1][4]
print()

# Отрицательные индексы
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print(spam[-3])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')
print()

# Получение части списка с помощью среза
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print()

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
print(spam[1:])
print(spam[:])
print(sorted(spam[3:]))
print('Срез')

# Получение длины списка с помощью функции len()
spam = ['cat', 'dog', 'moose']
print(len(spam))
print()

# Изменение значений в списках с помощью индексов
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)
print()

# Конкатенация и репликация списков
li = [1, 2, 3] + ['A', 'B', 'C']
print(li)
li = ['X', 'Y', 'Z'] * 3
print(li)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)
print()

# Удаление значений из списка с помощью инструкции del 
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[int(2.0)]
print(spam)



print()
for i in range(1, 10):
    list_card.append(i)

print(list_card[3])