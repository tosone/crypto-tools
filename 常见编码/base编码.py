#-*-coding:utf-8-*-


####base32
###################################################################################################
def base32():
	print('1.����\n2.����\n3.�˳�\n')
	select=int(raw_input('��ѡ��'))
	if select==1:
		import base64
		str=raw_input('����Ҫ���ܵ�base�ַ�����')
		print 'base64encod:',base64.b64encode(str)
		print 'base32encod:',base64.b32encode(str)
		print 'base16encod:',base64.b16encode(str)
		raw_input("���������������")
	elif select==2:
		strf=raw_input('����Ҫ�ƽ��base�ַ�����')
		import base64 

		try:
			base64.b64decode(strf).decode('utf-8')
			print 'base64decod:',base64.b64decode(strf).decode('utf-8')
		except :
			pass
		try:
			base64.b32decode(strf).decode('utf-8')
			print 'base32decod:',base64.b32decode(strf).decode('utf-8')
		except :
			passs
		try:
			base64.b16decode(strf)
			print 'base16decod:',base64.b16decode(strf).decode('utf-8')
		except :
			pass
		raw_input("���������������")
	else:
		import os
		os.system('cls')
		return
#############s######################################################################################

base32()
