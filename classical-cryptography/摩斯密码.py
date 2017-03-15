#!/usr/bin/env python
#-*-coding:utf-8-*-
# 摩斯密码
###################################################################################################


def mose():
    list = ('-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..')
    print('1.加密\n2.解密\n3.退出\n')
    select = int(raw_input('请选择：'))
    jia = ""
    if select == 1:
        input1 = raw_input('请您输入要加密的字符串：')
        print "加密后的为：",
        for i2 in input1:
            ord1 = ord(i2) - 87
            print list[ord1],
        print ''
    elif select == 2:
        input = raw_input('输入摩斯密文，注;中间用空格隔开：')
        f_input = input.split()
        ascil = ""
        for i in f_input:
            if i in list:
                asc = list.index(i) + 87
                ascil = ascil + chr(asc)
            else:
                print "%s 不是摩斯密文" % i
        print ascil
    else:
        import os
        os.system('cls')
        return
    raw_input("请输入任意键继续")
###################################################################################################
mose()
