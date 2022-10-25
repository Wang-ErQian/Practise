# 修改为完成练习 6-2 而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来
person_num = {'person_1': 1, 'person_2': 2, 'person_3': 3, 'person_4': 4, 'person_5': 5}
print("person_1: " + str(person_num['person_1']))
print("person_2: " + str(person_num['person_2']))
print("person_3: " + str(person_num['person_3']))
print("person_4: " + str(person_num['person_4']))
print("person_5: " + str(person_num['person_5']))
print("===========================================")
person_num['person_1'] = [1, 2, 3]
person_num['person_2'] = [4, 5, 6]
person_num['person_3'] = [7, 8, 9]
person_num['person_4'] = [11, 12, 13]
person_num['person_5'] = [14, 15, 16]
for person, numbers in person_num.items():
    print(person + "喜欢：")
    for number in numbers:
        print(number)

