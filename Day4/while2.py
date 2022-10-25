"""
用while循环实现1~100之间偶数求和
"""

sum = 0
num = 2
while sum <= 100:
    sum += num
    num += 2
print(sum)