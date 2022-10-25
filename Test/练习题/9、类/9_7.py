# 管理员是一种特殊的用户。
# 编写一个名为Admin 的类，让它继承你为完成练习9-3 或练习9-5 而编写的User 类。
# 添加一个名为privileges 的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为show_privileges()的方法，它显示管理员的权限。
# 创建一个Admin实例，并调用这个方法。
class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("姓:" + self.first_name + " 名:" + self.last_name + " 年龄:" + str(self.age))


    def greet_user(self):
        print("欢迎光临," + self.first_name + "" + self.last_name + "!")


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        if self.first_name == "root":
            print(self.privileges)
        else:
            print("You can`t do ")


admin = Admin('王', '二千', 23)
print(admin.describe_user())
print("你的权限：")
print(str(admin.show_privileges()))
