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

                print '����Ϊ : %s' % pwd
		fd=open('���ܺ�.txt','a')
		fd.write("\n"+file+"�ļ��������ǣ�\t"+pwd)
		fd.flush()
		fd.close()
		end = time.clock()

		print "�ƽ���ʱ : %f s" % (end - start)

		print "�����ƽ��¼�Ѿ����浽���ļ��С����ܺ�.txt��"

        except:

                return

def main():

	file = raw_input("������Ҫ�ƽ���ļ�·���磺C:\\file.zip��")

	dic = raw_input("�����������ֵ���ļ�·����")
	
	print '�����ƽ�...'

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