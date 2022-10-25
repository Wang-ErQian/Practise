# 编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It’s _____.”。
import json
fav_num = input("Please input your favorite number:\n")
file_path = 'fav_num.json'
with open(file_path, 'w') as file_obj:
    json.dump(fav_num, file_obj)

with open(file_path) as file_obj:
    num = json.load(file_obj)
    
print("I know your favorite number! It’s " + str(num) + ".")