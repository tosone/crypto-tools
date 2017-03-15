#-*-coding:utf-8-*-

####凯撒密码
###################################################################################################
def Caesar():

	print('1.带字符\n2.不带字符\n3.退出\n')
	select=int(raw_input('请选择：'))
	if select==1:
		lstr=raw_input("输入密文：")  
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
		print "1.输入移位个数\n2.移位26次\n3.退出"
		sss = int(raw_input("select:"))
		if sss == 1:
			nnn = int(raw_input("输入移位个数:"))
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
	raw_input("请输入任意键继续")
###################################################################################################
Caesar()
