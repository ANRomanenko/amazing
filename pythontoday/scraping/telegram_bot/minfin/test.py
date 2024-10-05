# for i in range(5):
#     print('Your name number: ('+ str(i) + ')')

# while True:
#     print("Who are you?")
#     name = input()
#     if name != "Joe":
#         continue
#     print("Hello, Joe. What is the password? (It is a fish)")
#     password = input()
#     if password == "swordfish":
#         break
# print("Access granted")

# name = ""

# while not name:
#     print("Enter your name:")
#     name = input()
# print("How many guests will you have?")
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have')
# print('Done') 

while True:
    print("Who are Joe")
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. What is the password?')
    password = input()
    if password == "swordfish":
        break

print("Acces granted")