# 设置变量 age 的值，再编写一个 if-elif-else 结构，根据 age的值判断处于人生的哪个阶段
age = 23
# 如果一个人的年龄小于 2 岁，就打印一条消息，指出他是婴儿
if age < 2:
    print("婴儿")
elif 4 > age >= 2:
    print("蹒跚学步")
elif 4 <= age < 13:
    print("儿童")
elif 13 <= age < 20:
    print("青少年")
elif 20 <= age < 65:
    print("成年人")
else:
    print("老年人")
