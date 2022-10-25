# 在完成练习 3-4~练习 3-7 时编写的程序之一中，使用 len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
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

# 使用 len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐
print("邀请了" + str(len(invite_list)) + "人")
