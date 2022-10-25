# 创建一个名为 Restaurant 的类，其方法__init__()设置两个属性：
# restaurant_name 和 cuisine_type。
# 创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant():

    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("停业抱歉！")

    def open_restaurant(self):
        print("欢迎光临!")


restaurant = Restaurant("蟹黄堡", "暂停营业")
print("餐厅：" + restaurant.restaurant + " 的营业状态：" + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant = Restaurant("蟹黄堡", "正在营业")
print("餐厅：" + restaurant.restaurant + " 的营业状态：" + restaurant.cuisine_type)
restaurant.open_restaurant()
