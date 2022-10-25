# 猜数字
import random

rand_num = random.randint(1, 100)
print("请输入一个1-100的正整数：\n")
for i in range(1, 101):
    num = input()
    if num > str(rand_num):
        print("太大")
    elif num < str(rand_num):
        print("太小")
    elif num == str(rand_num):
        print("正确")
        break
    else:
        print("请输入正整数")
