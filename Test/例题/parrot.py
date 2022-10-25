# message = input("111")
# print(message)

prompt = "123"
prompt += "223"
# message = ""
# while message != 'quit':
#     message = input(promt)
#     if message != 'quit':
#         print(message)

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
