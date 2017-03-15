#!/usr/bin/env python
#-*-coding:utf-8-*-

# qwe密码
##################################################################################################


def qwe():
    j = raw_input("input qwe密文:")
    z = ""
    for k in j:
        n = 0
        for i in "qwertyuiopasdfghjklzxcvbnm":
            n = n + 1
            if i == k:
                z = z + (chr(n + 96))
    print z
    raw_input("请输入任意键继续")
##################################################################################################
qwe()
