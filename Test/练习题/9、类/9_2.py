# 根据你为完成练习 9-1 而编写的类创建三个实例，并对每个实例调用方法 describe_restaurant()。
class Restaurant():

    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("非常抱歉！")

    def open_restaurant(self):
        print("欢迎光临!")


restaurant_1 = Restaurant("蟹黄堡", "暂停营业")
print("餐厅：" + restaurant_1.restaurant + " 的营业状态：" + restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_2 = Restaurant("比奇堡", "暂停营业")
print("餐厅：" + restaurant_2.restaurant + " 的营业状态：" + restaurant_2.cuisine_type)
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant("魔仙堡", "暂停营业")
print("圣地：" + restaurant_3.restaurant + " 的营业状态：" + restaurant_3.cuisine_type)
restaurant_3.describe_restaurant()