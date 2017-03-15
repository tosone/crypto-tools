#-*-coding:utf-8-*-


####md5解密
###################################################################################################
def md5():
	print('1.加密\n2.解密\n3.退出\n')
	select=int(raw_input('请选择：'))
	if select==1:
		import hashlib
		str=raw_input('输入要加密的字符串：')
		md5=hashlib.md5()
		md5.update(str)
		print md5.hexdigest(),str
		raw_input("请输入任意键继续")
	elif select==2:
		str1=raw_input('输入要解密的字符串：')
		str2=raw_input('输入字典文件名，注，字典需在本程序的同一目录：')
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
					raw_input("请输入任意键继续")
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