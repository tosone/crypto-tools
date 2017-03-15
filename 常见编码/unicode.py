def unicode():
	import re
	print('1.unicode转字符\n2.字符转unicode\n3.退出\n')
	select=int(raw_input("请选择："))
	z=""
	if select==1:
		input1=raw_input('请您输入unicode码：')
		print "字符串为：" ,
		b = re.split(r'[\s\,\;]+',input1)
		for i in b:
			i=int(i)
			i=unichr(i)
			z=z+i
		print z
	elif select==2:
		a = raw_input("请您输入字符串：")
		print "unicode为：",
		for i in a:
			print i 
		print z


unicode()
