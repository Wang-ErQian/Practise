# 将同一个数字乘三次称为立方。例如，在 Python 中，2 的立方用 2**3表示。
# 请创建一个列表，其中包含前 10 个整数（即 1~10）的立方，再使用一个 for 循环将这些立方数都打印出来。
test_list = []
for num in range(1, 11):
    num = num ** 3
    test_list.append(num)
print(test_list)
