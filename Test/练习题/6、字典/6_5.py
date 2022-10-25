# 创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt'。
# 使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
rivers = {'nile': 'egypt', 'amazon': 'america', 'yangtze': 'china'}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
print("=====================================================")
# 使用循环将该字典中每条河流的名字都打印出来。
for river in rivers.keys():
    print(river.title())
print("=====================================================")
# 使用循环将该字典包含的每个国家的名字都打印出来。
for country in rivers.values():
    print(country.title())