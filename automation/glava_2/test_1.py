print((5 > 4) and (3 == 5)) # False
print(not (5 > 4)) # False
print((5 > 4) or (3 == 5)) # True
print((True and True) and (True == False)) # False
print((not False) or (not True)) # True
print()

# spam = 5

# if spam == 5:
#     print('eggs')
#     if spam >= 5:
#         print('bacon')
#     else:
#         print('ham')
#     print('spam')
# print('spam')


# while True:
#     spam = input('Введите значение:\n')

#     if spam == 'Hello':
#         print('Hello World')
#         break
#     elif spam == 'Howdy':
#         print('Hello Howdy')
#         break
#     else:
#         print('Greetings')


for i in range(1, 10):
    print(i)

print()

i = 1

while i < 10:
    print(i)
    i += 1