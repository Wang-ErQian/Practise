"""
绘制小猪佩奇
"""
from turtle import *


def nose(x,y):
    """画鼻子"""
    penup()
    #将海龟移动到指定位置
    goto(x, y)
    pendown()
    #设置海龟的方向