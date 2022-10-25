# 在为完成练习 9-1 而编写的程序中，添加一个名为 number_served的属性，并将其默认值设置为 0。
# 根据这个类创建一个名为 restaurant 的实例；
# 打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它添加一个名为 set_number_served()的方法，它让你能够设置就餐人数。
# 调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为 increment_number_served()的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
class Restaurant():

    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type
        self.number_served = 0              # 添加一个名为 number_served的属性，并将其默认值设置为 0。

    def describe_restaurant(self):
        print("停业抱歉！")

    def open_restaurant(self):
        print("欢迎光临!")

    def set_number_served(self, set_number_eat):          # 添加一个名为 set_number_served()的方法，它让你能够设置就餐人数。
        print("就餐人数："+str(set_number_eat))

    def increment_number_served(self, up_number_eat):          # 添加一个名为 increment_number_served()的方法，它让你能够将就餐人数递增。
        self.number_served += up_number_eat


restaurant = Restaurant("蟹黄堡", "正在营业")          # 创建一个名为 restaurant 的实例；
restaurant.number_served = 10
print("餐厅："+restaurant.restaurant+" 状态："+restaurant.cuisine_type+" 已接待人数："+str(restaurant.number_served))   # 打印有多少人在这家餐馆就餐过，
restaurant.set_number_served(50)            #调用set_number_served方法并向它传递一个值，然后再次打印这个值。
restaurant.increment_number_served(50)
print("餐厅："+restaurant.restaurant+" 每日可接待人数："+str(restaurant.number_served))#调用increment_number_served方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
