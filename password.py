passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
typedPassword = input("Введите пароль: ")
if typedPassword == secretPassword:
    print('Доступ разрешён')
    if typedPassword == '12345':
        print('Рекомендуем установить более сложный пароль!')
else:
    print('В доступе отказано!')