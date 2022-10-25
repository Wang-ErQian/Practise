# 设置外星人的颜色，并编写一个 if-else 结构。
alien_color = 'green'
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5 个点。
if alien_color == 'green':
    print("玩家获得5分")
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了 10 个点。
if alien_color != 'green':
    print("玩家获得10分")
# 编写这个程序的两个版本，在一个版本中执行 if 代码块，而在另一个版本中执行 else 代码块。
if alien_color == 'green':
    print("玩家获得5分")
elif alien_color != 'green':
    print("玩家获得10分")
