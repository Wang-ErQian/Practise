# 创建一个名为 cities 的字典，其中将三个城市名用作键；
# 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含 country、population 和 fact 等键。
# 将每座城市的名字以及有关它们的信息都打印出来
cities = {
    '北京': {
        'country': 'China',
        'population': '2.19千万',
        'fact': '首都'
    },

    '上海': {
        'country': 'China',
        'population': '2.49千万',
        'fact': '魔都'
    },

    '深圳': {
        'country': 'China',
        'population': '1.76千万',
        'fact': '渔村'
    }
    }
for city, city_info in cities.items():
    print("==================================")
    print(city)
    for info in city_info:
        print(info)
