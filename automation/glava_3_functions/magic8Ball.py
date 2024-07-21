import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubful'
    
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune, f'- Равно цыфре: {r}')

# print(getAnswer(random.randint(1, 9))) # можно использовать и такой варинт кода
print()

spam = print('Hello')

print(None == spam)
print()

print('Hello ', end='')
print('World')
print()

print('cats', 'dogs', 'mice')
print()

print('cats', 'dogs', 'mice', sep=', ')
print()

car = ['audi', 'ford', 'mercedes', 'toyota', 'volkswagen']
for i in car:
    if i == 'mercedes':
        print('Mers')