"""
输出斐波那契数列的前20个数
"""
from re import A


a = 0
b = 1
for _ in range(20):
    a, b = b, a + b
    print(a, end=' ')