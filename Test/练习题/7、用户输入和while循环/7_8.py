# 创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；
# 再创建一个名为 finished_sandwiches 的空列表。
# 遍历列表 sandwich_orders，对于其中的每种三明治，都打印一条消息，
# 如 I made your tuna sandwich，并将其移到列表finished_sandwiches。
# 所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['草莓三明治', '香蕉三明治', '苹果三明治']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)