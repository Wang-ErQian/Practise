# 在你为完成练习 8-9 而编写的程序中，
# 编写一个名为make_great()的函数，
# 对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。
# 调用函数 show_magicians()，确认魔术师列表确实变了
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
show_magicians(make_great(magicians_list))
