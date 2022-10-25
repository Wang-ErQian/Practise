# 创建一个名为 favorite_places 的字典。在这个字典中，将三个人的名字用作键；
# 对于其中的每个人，都存储他喜欢的 1~3 个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来
favorite_places = {'张三': ['北京', '上海', '广州'], '李四': ["天津", "河北", "河南"], '王五': ["湖南", "湖北", "四川"]}
for people, favorite_place in favorite_places.items():
    print(people+ "喜欢：")
    for place in favorite_place:
        print(place)
    print("===========================================")