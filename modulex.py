#================= IO RELATED
import os
import sys
def fread(path):
	f=open(path,'r+',).read()
	return f

def fwrite(fname,content):
	f=open(fname,"w+",errors="ignore")
	f.write(content)

def fappend(fname,content):
	f=open(fname,"a+",errors="ignore")
	f.write(content)

def touch(fpath):
	check= os.path.exists(fpath)
	(lambda fname1:[open(fname1,"w+",errors="ignore").write(""),print('Touched',fname1)] 
		if not check else None) (fpath)

def softwrite(fname,content):
	f=open(fname,"w+").write(content) if not os.path.exists(fname)	else print('file exists, ricsk nai lene ka')

def cleanup():
	import shutil
	shutil.rmtree('__pycache__')






# =============== AUTO_PACKAGE
def auto_pip(mode,modulesList):
# automatically Instally Pip Packages Without Missing Module Error
	print('___autopip started___')
	import subprocess as sp
	# PRE PIP CHECK
	proc=sp.run('pip list',stdout=sp.PIPE,text=1)
	# consoleOUT=proc.stdout
	satisfied={x: (x in proc.stdout) for x in modulesList}
	pipInstallSignal=0
	pipUninstallSignal=0
	for k,v in satisfied.items():
		print(k+'\t> exists') if v else print(k,'is missing',end=' =|= ')
		if not v: pipInstallSignal=1  
		if v:pipUninstallSignal=1

	
	if mode=='download':
		proc=sp.run(f'pip download {" ".join(modulesList)} ' ,stdout=sp.PIPE	,shell=0)
		output=proc.stdout.read().decode('ascii').split('\n')
		print([x for x in output if 'Successfully' in x][0])
		proc.kill()
			
	if mode=='install': 
		if pipInstallSignal==True: 
			proc=sp.run('pip install {} -U'.format(" ".join(modulesList)),text=True,shell=1)
		else: return print(f'\n{modulesList} were already installed')

	if mode=='uninstall': 
		if pipUninstallSignal==True: 
			proc=sp.run('pip uninstall -y {}'.format(" ".join(modulesList)),text=True,shell=0,input='y\ny\ny\ny\ny\ny\n')
		else: return print(f'\n{modulesList} were already uninstalled')

	#CHECK SUCCESS OF PROCESS
	if proc.returncode==0:
		print('auto_pip Run Success')
		return proc.returncode

modules=['numpy','pandas','scikit-learn']
a=auto_pip('install',modules)
print(a)

try:
	import numpy
	pass
except Exception as e:
	print(e)
	exit()
arr=numpy.array([1,2,3,4,5])
print(arr)
print('____________NEW CODE BEGIN_______________')



# =============== Miscalleneous
def kill_code():
	import os
	os.kill(os.getpid(),signal.SIGABRT)
kill_switch=kill_code






# ===============JSON FUNCTIONS
import json
def jloads(string):
	#ret dict
	return json.loads(string)

def jdumps(dictonary):
	#ret string
	return json.dumps(dictonary,indent=4)

def jload(fromfile):
	#ret dict
	return json.load(open(fromfile))

def jdump(dictonary,toFile):
	#write to disk
	return json.dump(dictonary,open(toFile,"w+"),indent=4)






#=============== PARALLELISM
import threading
def threadQueue(workQueue,worker):
	pass






#===============WEB FUNCTIONS
def make_soup(markup):
	from bs4 import BeautifulSoup as soup
	return soup(markup,'html5lib')

def get_page(url,soupify=True):
	from bs4 import BeautifulSoup as soup
	import html5lib,requests
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	rawtext=requests.get(url,headers=headers).text
	if soupify==True:
		return soup(rawtext,'html5lib')
	else:
		return rawtext

def get_page_selenium(url,headless=True,strategy='normal'):
	from selenium import webdriver as wd
	opts = wd.firefox.options.Options();	
	opts.page_load_strategy = strategy
	if headless: opts.headless = True 
	# opts.add_argument("--headless") 		#works standalone
	try:
		client 	= wd.Firefox(options=opts);
		client.get(url);
		markup= client.page_source;
		return client,markup
	except Exception as e:	client.quit();	print("browser exit due to error"+str(e))

def push_tab(client,url):
	client.execute_script("window.open('{}', '_blank')".format(url))






#______________________________________________
#@#$%@#$%#$%#$%#+++CRYPTOGRAPHY+++#@$#@$#@$!@# 
import random
class Swamicrypt:
	def __init__(self, basepassword):
		self.basepassword= basepassword
		self.cryptSpace= self.generate_alphanumeric_chars()
		self.viewCryptSpace= lambda :"".join(self.cryptSpace)
		self.storage= self.cryptx()
		self.credentials= self.make_key(self.storage[0],self.storage[1])
# 
	def generate_alphanumeric_chars(self):
		rn=range
		space=  [chr(x) for x in rn(ord("0"),ord("9")+1)]
		space+= [chr(x) for x in rn(ord("a"),ord("z")+1)]
		space+= [chr(x) for x in rn(ord("A"),ord("Z")+1)]
		return space
# 
	def cryptx(self,security=4):
		def r(namespace,k=security): return random.sample(namespace,k=k)

		cryptSpace=self.cryptSpace
		keySpace=[r(cryptSpace,k=1)[0] for x in range(len(self.basepassword)*security)]
		keySpace="".join(keySpace)
		return (self.basepassword,keySpace)

	def make_key(self,stringx,keySpace):
		ks_indices=random.sample(list(enumerate(keySpace)) ,k=len(stringx))
		ord_add=[ord(s)+ord(p[1]) for s,p in zip(stringx,ks_indices)]
		key=[str(ki[0])+'+'+str(oa) for ki,oa in zip(ks_indices,ord_add)]
		key="-".join(key)
		return key,keySpace

	def decryptx(self,credentials):
		key,keyspace=credentials
		maps=key.split('-')
		imods=[x.split('+') for x in maps]
		originPass=[ chr(int(x[1]) - ord(keyspace[int(x[0])])) for x in imods ]
		return "".join(originPass)

if __name__ == '__main__':
	cryptonik=Swamicrypt("qwerty123")
	kp=cryptonik.credentials
	print([eval('eval(kp[0])'),kp][1])
	orignal=cryptonik.decryptx(kp)

	# fwrite('cryptEngineTest.txt',str(kp))