# 创建一个包含魔术师名字的列表，
# 并将其传递给一个名为show_magicians()的函数，
# 这个函数打印列表中每个魔术师的名字。
def show_magicians(magicians):
    """打印列表"""
    for magician in magicians:
        print(magician)


magicians_list = ['magician_1', 'magician_2', 'magician_3']
show_magicians(magicians_list)
