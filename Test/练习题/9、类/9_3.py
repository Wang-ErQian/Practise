# 创建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性。
# 在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("姓:"+self.first_name+" 名:"+self.last_name+" 年龄:"+self.age)

    def greet_user(self):
        print("欢迎光临,"+self.first_name+""+self.last_name+"!")


user_1 = User("王", "二千", "22")
user_1.describe_user()
user_1.greet_user()
