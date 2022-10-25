# 创建一个至少包含 5 个用户名的列表，且其中一个用户名为 'admin' 。
# 想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息
users = ['admin', 'user_1', 'user_2', 'user_3', 'user_4']
for user in users:
    if user == 'admin':
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again")
