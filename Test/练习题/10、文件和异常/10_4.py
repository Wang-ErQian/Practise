# 编写一个while 循环，提示用户输入其名字。
# 用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt 中。
# 确保这个文件中的每条记录都独占一行。

file_path = '../../guest_book.txt'
with open(file_path, 'a') as file:
    while 1:
        name = input("请输入姓名：\n")
        if name == "退出":
            break;
        else:
            file.write(name + "\n")
            print("Welcome, " + name + "！")