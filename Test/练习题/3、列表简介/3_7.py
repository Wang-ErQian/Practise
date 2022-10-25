# 你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾
invite_list = ['wangerqian', 'wangeq', 'weq']
print("there is a bigger table")
# 使用 insert()将一位新嘉宾添加到名单开头
invite_list.insert(0, "王二千")
# 使用 insert()将另一位新嘉宾添加到名单中间
invite_list.insert(2, "二千")
# 使用 append()将最后一位新嘉宾添加到名单末尾
invite_list.append("王")
print(invite_list[0] + " come on")
print(invite_list[1] + " come on")
print(invite_list[2] + " come on")
print(invite_list[3] + " come on")
print(invite_list[4] + " come on")
print(invite_list[5] + " come on")
# 你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾
# 在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息
print("only two can come")
# 使用 pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
# 每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐
print(invite_list.pop() + " can not come")
print(invite_list.pop() + " can not come")
print(invite_list.pop() + " can not come")
print(invite_list.pop() + " can not come")
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列
print(invite_list[0] + " come")
print(invite_list[1] + " come")
# 使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的
del invite_list[1]
del invite_list[0]
print(invite_list)
