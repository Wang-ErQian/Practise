# 编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt 中。
file_path = '../../guest.txt'
with open(file_path, 'a') as file_object:
    name = input("请输入姓名：\n")
    file_object.write(name+'\n')