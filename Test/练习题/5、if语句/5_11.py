# 序数表示位置，如 1st 和 2nd。大多数序数都以 th 结尾，只有 1、2 和 3例外。
# 在一个列表中存储数字 1~9
nums = range(1, 10)
# 遍历这个列表
# 在循环中使用一个 if-elif-else 结构，以打印每个数字对应的序数。
# 输出内容应为 1st 、 2nd 、 3rd 、 4th 、 5th 、 6th 、 7th 、 8th 和 9th ， 但每个序数都独占一行
for num in nums:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")
