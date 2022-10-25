# 为完成练习 5-8 编写的程序中，添加一条 if 语句，检查用户名列表是否为空
users = ['admin', 'user_1', 'user_2', 'user_3', 'user_4']
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again")
print("===========================================")
del users[:]
if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", thank you for logging in again")
else:
    print("We need to find some users!")