def unicode():
	import re
	print('1.unicodeת�ַ�\n2.�ַ�תunicode\n3.�˳�\n')
	select=int(raw_input("��ѡ��"))
	z=""
	if select==1:
		input1=raw_input('��������unicode�룺')
		print "�ַ���Ϊ��" ,
		b = re.split(r'[\s\,\;]+',input1)
		for i in b:
			i=int(i)
			i=unichr(i)
			z=z+i
		print z
	elif select==2:
		a = raw_input("���������ַ�����")
		print "unicodeΪ��",
		for i in a:
			print i 
		print z


unicode()
