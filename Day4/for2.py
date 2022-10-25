"""
用for循环实现1~100之间偶数求和
"""

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)