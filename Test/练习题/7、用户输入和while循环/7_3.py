# 让用户输入一个数字，并指出这个数字是否是 10 的整数倍
number = input("请输入一个数字")
if int(number) % 10 == 0:
    print("是10的倍数")
else:
    print("不是10的倍数")
