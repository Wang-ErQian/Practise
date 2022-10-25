# 随机生成1个3位数和1个2位数，从键盘输出这两个整数的和与差
import random

rand_3, rand_2 = random.randint(100, 1000), random.randint(10, 100)
print(rand_2, rand_3)
print("和：" + str(rand_2 + rand_3) + "\n差：" + str(rand_3 - rand_2))
