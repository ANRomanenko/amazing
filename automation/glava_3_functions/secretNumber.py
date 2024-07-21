import random

secretNumber = random.randint(1, 20)
print("Мною загадано число в интервале от 1 до 20. Попробуйте его отгадать")
print('Вам даётся для угадывания 6 попыток!\n')

for shans in range(1, 7):
    print("Ваш вариант:")
    guess = int(input())
    print(f"Попытка №: {shans}")

    if guess < secretNumber:
        print("Предположенное число меньше задуманного.\n")
    elif guess > secretNumber:
        print("Предположенное число больше задуманного.\n")
    else:
        break  # Соответствует правильному ответу

if guess == secretNumber:
    print("Верно! Количество попыток: " + str(shans))
else:
    print("Нет. Было задумано число: " + str(shans))

# def test(delenie):
#     try:
#         return 42 / delenie
#     except ZeroDivisionError:
#         print('Ошибка!')

# print(test(2))
# print(test(12))
# print(test(0))
# print(test(1))