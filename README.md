
# Documentation

## USAGE
put mxproxy.py file in your code folder, keep it adjacent to file where you want to import, and to import modulex, you need to use this command 

	from mxproxy import mx 

after that you can stat using modulex's all function and speedup all the repetitive tasks.
functions available in Modulex. for example you have a file called mycode.py content below.

	from mxproxy import mx
	
	data=mx.fread('myfile.txt')
	print(data)

	jsondata=mx.jload('myjsonfile.json')
	print(jsondata)

