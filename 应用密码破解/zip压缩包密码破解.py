#-*-coding:utf-8-*-
import time
import sys



'''

z = zipfile.ZipFile('') , extractall

z.extractall(pwd)

'''

import zipfile

import threading

 

def zipbp(file,zfile, pwd, start):

        try:

                zfile.extractall(pwd=pwd)

                print '密码为 : %s' % pwd
		fd=open('解密后.txt','a')
		fd.write("\n"+file+"文件的密码是：\t"+pwd)
		fd.flush()
		fd.close()
		end = time.clock()

		print "破解用时 : %f s" % (end - start)

		print "密码破解记录已经保存到此文件夹“解密后.txt”"

        except:

                return

def main():

	file = raw_input("请输入要破解的文件路径如：C:\\file.zip：")

	dic = raw_input("请输入密码字典的文件路径：")
	
	print '正在破解...'

        zfile = zipfile.ZipFile(file)

        pwdall = open(dic)
	start = time.clock()
        for pwda in pwdall.readlines():

                pwd = pwda.strip('\n')

                t = threading.Thread(target=zipbp, args=(file,zfile, pwd,start))

                t.start()

                t.join()

if __name__ == '__main__':

        main()