#-*-coding:utf-8-*-


####md5����
###################################################################################################
def md5():
	print('1.����\n2.����\n3.�˳�\n')
	select=int(raw_input('��ѡ��'))
	if select==1:
		import hashlib
		str=raw_input('����Ҫ���ܵ��ַ�����')
		md5=hashlib.md5()
		md5.update(str)
		print md5.hexdigest(),str
		raw_input("���������������")
	elif select==2:
		str1=raw_input('����Ҫ���ܵ��ַ�����')
		str2=raw_input('�����ֵ��ļ�����ע���ֵ����ڱ������ͬһĿ¼��')
		import hashlib
		import time
		start = time.clock()
		md5=hashlib.md5()
		p=file(str2)
		p.close
		p=file(str2)
		while True:
			n = p.readlines().strip('\n')
			if len(n)!=0:
				import hashlib
				md5=hashlib.md5()
				md5.update(n)
				if str1 in md5.hexdigest():
					print md5.hexdigest(),n

					end = time.clock()
					print "read: %f s" % (end - start)
					raw_input("���������������")
					import os
					os.system('cls')
					return
			else:
				end = time.clock()
				print "not found\nread: %f s" % (end - start)
				import os
				os.system('cls')
				return
	else:
		import os
		os.system('cls')
		return
###################################################################################################

md5()