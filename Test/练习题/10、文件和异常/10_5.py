# 编写一个while 循环，询问用户为何喜欢编程。
# 每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
file_path = '../../why.txt'
with open(file_path, 'a') as file:
    while 1:
        reason = input("Why do you like Coding?\n")
        if reason == "quit":
            break;
        else:
            file.write(reason + "\n")
