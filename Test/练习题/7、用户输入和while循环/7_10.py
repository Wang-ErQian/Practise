# 编写一个程序，调查用户梦想的度假胜地。
# 使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。
reports = {}
active = True
while active:
    name = input("你叫什么名字？\n")
    response = input("If you could visit one place in the world, where would you go?\n")
    reports[name] = response
    report = input("还有人要参与吗？\n")
    if report == 'no':
        active = False
print("================================")
for name, response in reports.items():
    print(name + " like " + response)
