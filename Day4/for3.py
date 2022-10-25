"""
输入非负整数n计算n！
"""

from unittest import result


n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d != %d' % (n, result))