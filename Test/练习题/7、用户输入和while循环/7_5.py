# 有家电影院根据观众的年龄收取不同的票价：
# 不到 3 岁的观众免费；
# 3~12 岁的观众为 10 美元；
# 超过 12 岁的观众为 15 美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价
age = input("请输入年龄:\n")
active = True
while active:
    if int(age) < 3:
        print("免费")
    elif int(age) < 12:
        print("10美元")
    else:
        print("15美元")
    break