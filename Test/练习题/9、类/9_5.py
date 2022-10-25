# 在为完成练习 9-3 而编写的 User 类中，添加一个名为login_attempts 的属性。
# 编写一个名为 increment_login_attempts()的方法，它将属性login_attempts 的值加 1。
# 再编写一个名为 reset_login_attempts()的方法，它将属性login_attempts 的值重置为 0。
# 根据 User 类创建一个实例，再调用方法 increment_login_attempts()多次。
# 打印属性 login_attempts 的值，确认它被正确地递增；
# 然后，调用方法 reset_login_attempts()，并再次打印属性 login_attempts 的值，确认它被重置为 0。
class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0  # 添加一个名为login_attempts 的属性。

    def describe_user(self):
        print("姓:" + self.first_name + " 名:" + self.last_name + " 年龄:" + self.age)

    def greet_user(self):
        print("欢迎光临," + self.first_name + "" + self.last_name + "!")

    def increment_login_attempts(self):  # 将属性login_attempts 的值加 1。
        self.login_attempts += 1

    def reset_login_attempts(self):  # 将属性login_attempts 的值重置为 0
        self.login_attempts = 0


user = User("王", "二千", 22)  # 根据 User 类创建一个实例
user.increment_login_attempts()
user.increment_login_attempts()  # 调用方法 increment_login_attempts()多次。
user.increment_login_attempts()
print("Login_attempts:" + str(user.login_attempts))  # 打印属性 login_attempts 的值，确认它被正确地递增；
user.reset_login_attempts()  # 调用方法 reset_login_attempts()
print("Login_attempts:" + str(user.login_attempts))  # ，再次打印属性 login_attempts 的值，确认它被重置为 0。
