#-*-coding:utf-8-*-


####希尔密码
##################################################################################################

def xier():
	import re
	import os
	import numpy 


####求逆矩阵

	a=raw_input("输入加密矩阵\n例如：\n[1,2,3]\n[4,5,6]\n[7,8,9]\n输入方式为:1，2，3，4，5，6，7，8，9\n请输入加密矩阵b:")
	z=re.split(r'[\s\,\;]+',a)

	for p in range (len(z)):
		if p*p == len(z):break

	len1 = len(z)/p
	b=zeros((p,len1))
	k=0
	for i in range (p):
		for j in range (len1):
			b[i][j] = z[k]
			k=k+1
	b = mat(b).I
	b1= b.T

###把输入变成矩阵

	input = raw_input("输入加密字符串a:")
	n = len(input)/p

	comp = int(raw_input("请选择\n1.a=0\n2.a=1\n:"))

	if comp == 1:asi = 97
	else:asi = 96
	print asi

	input = list(input)
	ss=zeros((n,len(input)/n))
	j=0

	for i in range (n) :
		for z in range (len(input)/n):

			ss[i][z]=ord(input[j])-asi
			j=j+1

	a=mat(ss)

####矩阵相乘乘以27

	c=dot(a,b)
	c1=dot(a,b1)

	c=c*27
	c1=c1*27

######输出结果

	def output(c):
	
        	dd=""
       	 	for i in range (c.shape[0]):
        	        for j in range (c.shape[1]):
                	        d = c[i,j]%26
        			e = d+asi
        			e = int(float(str(e)))
                		dd=dd+chr(e)
      		return dd

	print output(c)
	print output(c1)

##############################################################################################################
xier()
raw_input("请输入任意键继续")