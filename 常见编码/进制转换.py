#-*-coding:utf-8-*-
import re
def ascii():

	input1=raw_input('��������Ҫת�����ַ���')
	bi=""
	oc=""
	int1=""
	he=""
	b = re.split(r'[\s\,\;]+',input1)
	print('������ַ�������Ϊ:\n1.������\n2.�˽���\n3.ʮ����\n4.ʮ������')
	xxx=int(raw_input("��ѡ��"))
	for o in b:
		if xxx==1:
			i=int(o,2)
			oo=oct(i)
			h=hex(i)
			bi=bi+" "+str(o)
			oc=oc+" "+oo
			int1=int1+" "+str(i)
			he=he+" "+h
		elif xxx==2:
			i=int(o,8)
			b=bin(i).replace('0b', '')
			h=hex(i)
			bi=bi+" "+str(b)
			oc=oc+" "+o
			int1=int1+" "+str(i)
			he=he+" "+h
		elif xxx==3:
			i=int(o)
			b=bin(i).replace('0b', '')
			o=oct(i)
			h=hex(i)
			bi=bi+" "+str(b)
			oc=oc+" "+o
			int1=int1+" "+str(i)
			he=he+" "+h
		elif xxx==4:
			if '0x' in o:
				o=o.replace('0x','')
			o='0x'+o
			i=int(o,16)
			b=bin(i).replace('0b', '')
			oo=oct(i)
			bi=bi+" "+str(b)
			oc=oc+" "+oo
			int1=int1+" "+str(i)
			he=he+" "+o
	print "������Ϊ��"+bi
	print "�˽���Ϊ��"+oc
	print "ʮ����Ϊ��"+int1
	print "ʮ������Ϊ��"+he
	raw_input("����������˳�")

try:	
	ascii()
except :
	print "ѡ��Ľ��Ʋ�ƥ��"