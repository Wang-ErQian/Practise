# 在本节中，为节省篇幅，程序 foods.py 的每个版本都没有使用for 循环来打印列表。
# 请选择一个版本的 foods.py，在其中编写两个 for 循环，将各个食品列表都打印出来
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
for food in friend_foods:
    print(food)
for food in my_foods:
    print(food)
