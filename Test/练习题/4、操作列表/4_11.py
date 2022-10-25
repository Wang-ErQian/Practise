# 创建食物列表的副本，并将其存储到变量friend_foods中，再完成如下任务
food_list = ['饭', '面', '包子', '馒头']
friend_foods = food_list[:]
# 在原来的列表中添加一种
food_list.append('西北风')
# 在列表 friend_pizzas 中添加另一种比萨
friend_foods.append('山珍海味')
print("My food:")
for food in food_list:
    print(food)
print("My friend`s list:")
for food in friend_foods:
    print(food)
