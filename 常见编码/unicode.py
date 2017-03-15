def unicode():
	import re
	print('1.unicode×ª×Ö·û\n2.×Ö·û×ªunicode\n3.ÍË³ö\n')
	select=int(raw_input("ÇëÑ¡Ôñ£º"))
	z=""
	if select==1:
		input1=raw_input('ÇëÄúÊäÈëunicodeÂë£º')
		print "×Ö·û´®Îª£º" ,
		b = re.split(r'[\s\,\;]+',input1)
		for i in b:
			i=int(i)
			i=unichr(i)
			z=z+i
		print z
	elif select==2:
		a = raw_input("ÇëÄúÊäÈë×Ö·û´®£º")
		print "unicodeÎª£º",
		for i in a:
			print i 
		print z


unicode()
