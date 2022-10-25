# 使用为完成练习 7-8 而创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。
# 在程序开头附近添加这样的代码:
# 打印一条消息，指出熟食店的五香烟熏牛肉卖完了；
# 再使用一个 while 循环将列表 sandwich_orders 中的'pastrami'都删除。
# 确认最终的列表 finished_sandwiches 中不包含'pastrami'。
sandwich_orders = ['草莓三明治', '香蕉三明治', '苹果三明治', 'pastrami', 'pastrami', 'pastrami']
print("pastrami 卖完了!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)