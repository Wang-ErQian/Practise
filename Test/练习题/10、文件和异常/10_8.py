# 创建两个文件cats.txt 和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# 将这些代码放在一个try-except 代码块中，以便在文件不存在时捕获FileNotFound 错误，并打印一条友好的消息。
# 将其中一个文件移到另一个地方，并确认except 代码块中的代码将正确地执行
try:
    with open('../../cats.txt') as file1:
        cats = file1.readlines()
        print(cats)
except FileNotFoundError:
    print("file not found")

try:
    with open('../../dogs.txt') as file2:
        dogs = file2.readlines()
        print(dogs)
except FileNotFoundError:
    print("file not found")

