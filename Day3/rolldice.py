"""
掷骰子决定做什么事
"""
from random import randint
from unittest import result

face = randint(1, 6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
elif face == 6:
    result = '讲冷笑话'
print(result)