responses = {}
polling_active = True
while polling_active:
    name = input("你叫啥\n")
    response = input("你喜欢哪座山\n")
    responses[name] = response
    repeat = input("还有人要来吗?\n")
    if repeat == 'no':
        polling_active = False
for name, response in responses.items():
    print(name + "\t" + response)
