# 你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。

# 以完成练习3_4时编写的程序为基础，在程序末尾添加一条 print 语句，指出哪位嘉宾无法赴约。
invite_list = ['王二千', '二千', '王']
print(invite_list[0] + " come on")
print(invite_list[1] + " come on")
print(invite_list[2] + " come on")
print(invite_list[2] + "can not come")

# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
invite_list[2] = 'wangerqian'
print(invite_list[0] + " come on")
print(invite_list[1] + " come on")
print(invite_list[2] + " come on")
