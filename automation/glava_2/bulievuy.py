# Булевые операторы and, or, not

# Оператор and
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print()

# Оператор or
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
print()

# Оператор not
# Оператор not, в отличие от операторов and и or, воздейуствует только на одно булево значение (выражение)
# и поэтому является унарным. Этот оператор обращает булево значение в его противоположность.
print(not True) # False
print(not not not not True) # True
print(not True) # False
print(not False) # True
print(True and True and not False) # True
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2) # True
print(not False and True and True) # True
# Как и для математических операторов, для булевых операторов оперделен порядок выполнения. После токо как будут вычеслены
# Все математические операторы и операторы сравнения, первыми выпоняются операторы not, затем - операторы and и только после
# Этого - операторы or