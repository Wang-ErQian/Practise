# 编写一个名为Privileges 的类，它只有一个属性——privileges，其中存储了练习9-7 所说的字符串列表。
# 将方法show_privileges()移到这个类中。
# 在Admin类中，将一个Privileges 实例用作其属性。
# 创建一个Admin 实例，并使用方法show_privileges()来显示其权限。
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
        privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("你有以下权限: " + self.privileges)

class Admin(Privileges):
    def __init__(self, privileges):
        self.privileges = privileges
        privilege = Privileges("can add post")
        self.privilege = privilege

admin = Admin("can add post")
print(admin.show_privileges())