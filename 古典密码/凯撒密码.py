#-*-coding:utf-8-*-

####��������
###################################################################################################
def Caesar():

	print('1.���ַ�\n2.�����ַ�\n3.�˳�\n')
	select=int(raw_input('��ѡ��'))
	if select==1:
		lstr=raw_input("�������ģ�")  
		for p in range(127):  
			str1 = ''  
			for i in lstr:  
				temp = chr((ord(i)+p)%127)  
				if 32<ord(temp)<127 :  
					str1 = str1 + temp   
					feel = 1  
				else:  
					feel = 0  
					break  
 			if feel == 1:  
				print(str1) 
		
	elif select==2:

		input = raw_input("input:")
		input = input.lower()
	
		b=map(ord,input)
		k=0
	
		while k < len(b):
			b[k]=b[k] -97
			k=k+1
		string=""
		print "1.������λ����\n2.��λ26��\n3.�˳�"
		sss = int(raw_input("select:"))
		if sss == 1:
			nnn = int(raw_input("������λ����:"))
			for i in b:
				i = (i+nnn)%26+97
				string=string+chr(i)
				print string
	
		if sss ==2:
			for j in range(1,26):
				string=""
				for i in b:
        				i=(i+j)%26+97
        				c=chr(i)
        				string=string+c
    				print string
	raw_input("���������������")
###################################################################################################
Caesar()
