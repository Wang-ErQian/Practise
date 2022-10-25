# 创建一个至少包含 5 个用户名的列表，并将其命名为 current_users
current_users = ['user_1', 'user_2', 'user_3', 'user_4', 'user_5']
# 创建一个包含 5 个用户名的列表，将其命名为 new_users ，并确保其中有一两个用户名也包含在列表 current_users 中
new_users = ['user_1', 'user_3', 'user_6', 'user_7', 'user_8']
# 遍历列表 new_users ，对于其中的每个用户名，都检查它是否已被使用。
# 如果是这样，就打印一条消息，指出需要输入别的用户名；
# 否则，打印一条消息，指出这个用户名未被使用
for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print("Please select another user name")
    else:
        print("You can use this name")
# 确保比较时不区分大消息；换句话说，如果用户名 'John' 已被使用，应拒绝用户名 'JOHN'
