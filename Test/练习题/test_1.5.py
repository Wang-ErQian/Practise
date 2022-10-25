# 使用time函数，编写程序求以下程序段的执行时间
import time

time_start = time.time()
sum_a = 0
for i in range(1, 10000 + 1):
    sum_a = sum_a + i
print(sum_a)
time_end = time.time()
time_spend = time_end - time_start
print(time_spend)
