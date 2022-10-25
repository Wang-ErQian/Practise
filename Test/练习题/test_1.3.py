# 使用turtle库函数，绘制五个不同半径的同切圆
import turtle

# turtle.circle(10)
# turtle.circle(20)
# turtle.circle(30)
# turtle.circle(40)
# turtle.circle(50)

for i in range(6):
    turtle.circle(0 + 10 * i)
turtle.mainloop()
