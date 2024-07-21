def collatz(number):
    while paste():
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1

# print('Enter number:')
# numbr = int(input())
# fort = collatz(numbr)
# print(fort)


def paste():
    print('Enter number:')
    numbr = int(input())
    return numbr

print(collatz(paste()))