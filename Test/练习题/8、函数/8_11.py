# 修改你为完成练习 8-10 而编写的程序，在调用函数make_great()时，向它传递魔术师列表的副本。
# 由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
# 分别使用这两个列表来调用 show_magicians()，确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the Great”的魔术师名字
def show_magicians(magicians):
    """打印列表"""
    for magician in magicians:
        print(magician)


def make_great(magicians_change):
    new_magicians = []
    while magicians_change:
        magician = magicians_change.pop()
        new_magician = 'The great ' + magician
        new_magicians.append(new_magician)
    return new_magicians


magicians_list = ['magician_1', 'magician_2', 'magician_3']
new_magicians = make_great(magicians_list[:])
show_magicians(magicians_list)
show_magicians(new_magicians)

