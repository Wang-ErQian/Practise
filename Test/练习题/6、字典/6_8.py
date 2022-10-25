# 创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；
# 在每个字典中，包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为 pets 的列表中，再遍历该列表，并将宠物的所有信息都打印出来
cat_1 = {'cat_1_1': 'person_1'}
cat_2 = {'cat_2_1': 'person_1'}
cat_3 = {'cat_3_1': 'person_1'}
pets = [cat_1, cat_2, cat_3]
for pet in pets:
    print(pet)

