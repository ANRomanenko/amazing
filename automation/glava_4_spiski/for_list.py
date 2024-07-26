# Использование циклов for со списками
for i in range(4):
    print(i)

print()


for i in [0, 1, 2, 3]:
    print(i)

print()

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print()

# Операторы in и not int
text = 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
print(text) # True

spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam) # False
print('howdy' not in spam) # False
print('cat' not in spam) # True