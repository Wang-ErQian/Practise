"""
用户身份验证
"""

# import getpass
# from getpass import getpass
# from getpass import *

username = input('请输入用户名：')
password = input('请输入密码：')
# 输入口令时终端没有回显
# password = getpass.getpass('请输入密码：')
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')