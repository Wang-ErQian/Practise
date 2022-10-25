# 选择一个程序，在末尾添加几行代码，以完成如下任务。
invite_list = ['wangerqian', 'wangeq', 'weq', 'zhang', 'zhao', 'chen']
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
front_three = invite_list[:3]
print("The first three items in the list are:")
print(front_three)
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
mid_three = invite_list[2:5]
print("Three items from the middle of the list are:")
print(mid_three)
# 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素
last_three = invite_list[-3:]
print("The last three items in the list are:")
print(last_three)
