# 将练习10-11 中的两个程序合而为一。
# 如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期的那样工作。
import json
file_path = 'fav_num.json'


def write_json():
    fav_num = input("Please input your favorite number:\n")
    with open(file_path, 'w') as file_obj:
        json.dump(fav_num, file_obj)
    read_json()


def read_json():
    with open(file_path) as file_obj:
        num = json.load(file_obj)
    print("I know your favorite number! It’s " + str(num) + ".")


def show_num():
    try:
        with open(file_path) as file_obj:
            num = json.load(file_obj)
            print("You favorite num is: " + str(num))
    except FileNotFoundError:
        write_json()


show_num()