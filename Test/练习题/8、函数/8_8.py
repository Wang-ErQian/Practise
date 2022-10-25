# 在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户输入一个专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数 make_album()，并将创建的字典打印出来。
# 在这个 while 循环中，务必要提供退出途径。
def make_album(singer, album, songs=''):
    if songs:
        album_info = {'singer:': singer, 'albun': album, 'songs':songs}
    else:
        album_info = {'singer:': singer, 'albun': album}
    return album_info


active = True
while active:
    singer_input = input("请输入歌手：\n")
    songs_input = input("请输入专辑：\n")
    album_new = make_album(singer_input, songs_input)
    print(album_new)
    active_bool = input("是否要继续?（Y/N)\n")
    if active_bool == 'N':
        active = False
