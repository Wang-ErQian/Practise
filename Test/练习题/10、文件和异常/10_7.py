# 将你为完成练习10-6 而编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。
while True:
    try:
        num1 = input("请输入一个数字：\n")
        num1 = int(num1)
        num2 = input("请输入一个数字：\n")
        num2 = int(num2)
        break
    except ValueError:
        print("你输入的不是数字！")
sum1 = num1 + num2
print("和为：" + str(sum1))