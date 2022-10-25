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

