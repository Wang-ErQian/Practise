# 修改你在练习10-8 中编写的except 代码块，让程序在文件不存在时一言不发。
try:
    with open('../../cats.txt') as file1:
        cats = file1.readlines()
        print(cats)
except FileNotFoundError:
    pass

try:
    with open('../../dogs.txt') as file2:
        dogs = file2.readlines()
        print(dogs)
except FileNotFoundError:
    pass