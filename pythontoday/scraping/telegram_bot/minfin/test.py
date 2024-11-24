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

# while True:
#     print("Who are Joe")
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello Joe. What is the password?')
#     password = input()
#     if password == "swordfish":
#         break

# print("Acces granted")

import requests

def get_requests_encoding():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }

    url = "https://8.8.8.8"
    host = "https://minfin.com.ua"

    r = requests.get(url=url, headers=headers)
    print(r.encoding)

get_requests_encoding()