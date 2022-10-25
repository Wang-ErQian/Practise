# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
investigation_list = ['sarah', 'edward']
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。
# 对于还未参与调查的人，打印一条消息邀请他参与调查
for people in favorite_languages.keys():
    if people in investigation_list:
        print("Thank you! " + people)
    else:
        print("Please under investigation " + people)
