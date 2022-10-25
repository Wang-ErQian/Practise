promp = "\n请输入一个你去过的城市:\n"
promp += "输入“quit”结束\n"

while True:
    city = input(promp)
    if city == 'quit':
        break
    else:
        print("我爱去" + city.title() + "!")
