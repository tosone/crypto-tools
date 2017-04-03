#!/usr/bin/env python
#-*-coding:utf-8-*-
import re


def ascii():

    input1 = raw_input('请您输入要转换的字符：')
    bi = ""
    oc = ""
    int1 = ""
    he = ""
    b = re.split(r'[\s\,\;]+', input1)
    print('输入的字符串进制为:\n1.二进制\n2.八进制\n3.十进制\n4.十六进制')
    xxx = int(raw_input("请选择："))
    for o in b:
        if xxx == 1:
            i = int(o, 2)
            oo = oct(i)
            h = hex(i)
            bi = bi + " " + str(o)
            oc = oc + " " + oo
            int1 = int1 + " " + str(i)
            he = he + " " + h
        elif xxx == 2:
            i = int(o, 8)
            b = bin(i).replace('0b', '')
            h = hex(i)
            bi = bi + " " + str(b)
            oc = oc + " " + o
            int1 = int1 + " " + str(i)
            he = he + " " + h
        elif xxx == 3:
            i = int(o)
            b = bin(i).replace('0b', '')
            o = oct(i)
            h = hex(i)
            bi = bi + " " + str(b)
            oc = oc + " " + o
            int1 = int1 + " " + str(i)
            he = he + " " + h
        elif xxx == 4:
            if '0x' in o:
                o = o.replace('0x', '')
            o = '0x' + o
            i = int(o, 16)
            b = bin(i).replace('0b', '')
            oo = oct(i)
            bi = bi + " " + str(b)
            oc = oc + " " + oo
            int1 = int1 + " " + str(i)
            he = he + " " + o
    print "二进制为：" + bi
    print "八进制为：" + oc
    print "十进制为：" + int1
    print "十六进制为：" + he
    raw_input("输入任意键退出")

try:
    ascii()
except:
    print "选择的进制不匹配"
