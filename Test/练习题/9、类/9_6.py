# 冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。
# 这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。
# 添加一个名为 flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。
# 创建一个IceCreamStand 实例，并调用这个方法。
class Restaurant():

    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        state = str(self.restaurant) + ' ' + str(self.cuisine_type)
        print(state + " 停业抱歉")

    def open_restaurant(self):
        state = str(self.restaurant) + ' ' + str(self.cuisine_type)
        print(state + ' 正在营业!')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant, cuisine_type):
        super().__init__(restaurant, cuisine_type)
        self.flavors = ['草莓', '苹果', '蓝莓', '葡萄']

    def show_icecream(self):
        for flavor in self.flavors:
            print(flavor)

icecreamstand = IceCreamStand('密雪冰城', '营业状态').open_restaurant()
print("我们有以下口味：")
food_list = IceCreamStand('密雪冰城', '正在营业').show_icecream()
