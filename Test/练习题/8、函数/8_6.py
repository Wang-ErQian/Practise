# 编写一个名为 city_country()的函数，它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面这样的字符串：
# "Santiago, Chile"
# 至少使用三个城市,国家对调用这个函数，并打印它返回的值。
def city_country(city="Santiago", country="Chile" ):
    """返回城市及归属国家"""
    print(city + "," + country)


city_country()
city_country("Beijing", "China")
city_country("Shenzhen", "China")
