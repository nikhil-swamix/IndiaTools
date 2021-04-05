#================= IO RELATED
import os
import random


#---------------------------
def setload(path,seperator='\n'):
	return set(fread(path).split(seperator))

def setwrite(path,setDataType):
	fwrite(path,"\n".join(setDataType))

def setupdate(path,newset):
	diff=newset - setload(path)
	fappend(path,diff)

#---------------------------
def fread(path):
	f=open(path,'r+',encoding='utf-8').read()
	return f

def fwrite(fpath,content):
	f=open(fpath,"w+",errors="ignore")
	f.write(content)

def fappend(fname,content):
	f=open(fname,"a+",errors="ignore")
	f.write(content+'\n')

def touch(fpath):
	head=os.path.split(fpath)[0]
	os.makedirs(head,exist_ok=True)
	if not os.path.exists(fpath):
		open(fpath,"w+",errors="ignore").close()
		print('Touched',fpath)

def list_files_timesorted(folder):
	jobFileQueue=[folder+x for x in os.listdir(folder)]
	jobFileQueue.sort(key=os.path.getmtime)
	return (jobFileQueue)

#------------------RANDOMIZERS
def randindex(L):
	return random.randrange(len(L)) # get random index

def poprandom(L):
	i = randindex(L) 
	L[i], L[-1] = L[-1], L[i] # swap with the last element
	return L.pop() # pop last element O(1)

def shuffle(L):
	return [pickrandom(L) for x in range(len(L))]

# =============== AUTO_PACKAGE
def auto_pip(modulesList,mode='install'):
	'''
		+DOC: 
			automatically Install Pip Packages With Missing Module && upgrades pip if its old, 
		+USAGE: 
			auto_pip('mode',[modules,...]) #where mode can be {install,uninstall,download} and modules is
			auto_pip('install',['pytorch','numpy','etc...']) 
		+NOTES: downloading can be useful if want to install later 
		from local source and avoid network cost.
	'''
	modulesList=[modulesList] if isinstance(modulesList,str) else modulesList
	import subprocess as sp
	#>>> preflight check && upgrade if old
	proc=sp.run('pip list',stdout=sp.PIPE,stderr=sp.PIPE,text=1)
	if 'You should consider upgrading' in proc.stderr:
		upgradeCommand=proc.stderr.split('\'')
		sp.run(upgradeCommand[1])

	pipInstallSignal,pipUninstallSignal= 0,0 #declare signals as 0,
	#below dict-> true if module present against module name ex: numpy:True
	satisfied={x:(x.lower() in proc.stdout.lower()) for x in modulesList} 
	for k,v in satisfied.items():
		print(k+'\t:preinstalled') if v else print(k,'is missing',end=' =|= ')
		if v==False: pipInstallSignal=1  
		if v==True: pipUninstallSignal=1 #NAND Condition if true then start uninstalling
	
	if mode=='download':
		proc=sp.run(f'pip download {" ".join(modulesList)} ' ,stdout=sp.PIPE	,shell=0)
		output=proc.stdout.read().decode('ascii').split('\n')
		print([x for x in output if 'Successfully' in x][0])
		proc.kill()
			
	if mode=='install': 
		if pipInstallSignal==True: 
			proc=sp.run('pip install {} -U'.format(" ".join(modulesList)),text=True,shell=1)
		else: print(f'{modulesList} were already installed'); return 1 

	if mode=='uninstall': 
		if pipUninstallSignal==True: 
			proc=sp.run('pip uninstall -y {}'.format(" ".join(modulesList)),text=True,shell=0)
		else: print(f'\n{modulesList} were already uninstalled'); return 1

	#CHECK SUCCESS OF PROCESS
	if proc.returncode==0:
		print('auto_pip Run Success')
		return proc.returncode

# =============== Miscalleneous
class Cache: 
	'''
		CREATES CACHE to save future calls cost
	'''
	pass

# ===============JSON FUNCTIONS
import json
def jloads(string): #return dict
	return json.loads(string)
def jload(path): #return dict
	return json.load(open(path))

def jdumps(dictonary,indent=4): #return string
	return json.dumps(dictonary,indent=indent)
def jdump(dictonary,path): #write to disk
	return json.dump(dictonary,open(path,"w+"),indent=4)

def jloadlines(path):
	jsonlines=open(path,'r').readlines()
	jldict={}
	for w in jsonlines:
		try: jldict.update(jloads(w))
		except: pass
	return jldict

def jdumplines(dictonary,indent=None): #return string
	return json.dumps(dictonary,indent=indent)


#---------------------------
def hash_db(hashkey,*hashvalue,dirname='./LOCAL_DATABASE/'):
	''' 
		if : an index(hashkey) is given then check is file exists and open and return a dict{}
		else : if second argument (hashvalue[]) is given then create a dict
	'''

	path=dirname+hashkey

	try:
		return jload(path)
	except Exception as e:
		if hashvalue:#write inputted value to memory
			fwrite(path,jdumps(hashvalue[0]))


#=============== PARALLELISM

class Parallelizer:
	def tpoolstart(fn,threadCount):
		pool=[threading.Thread(target=fn) for x in range(threadCount)]
		print(f'INFO: Starting {threadCount} threads')
		[x.start() for x in pool]
		return pool

	def tpooljoin(tp):
		[x.join() for x in tp]


	def tpoolexec(fn,threadCount=50):
		Parallelizer.tpooljoin(Parallelizer.tpoolstart(fn,threadCount))





#===============WEB FUNCTIONS

import requests	
def make_session_pool(count=1):
	return [requests.Session() for x in range(count)]

def get_page(url,headers={}): #return a page req object and retrive text later
	UserAgent={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}

	headers.update(UserAgent)
	# print(headers)
	# spoofBrowser = {'User-Agent': UA,'Cookie':Cookie}
	# headers=headers
	req=requests.get(url,headers=headers)
	if not req: #send headers only when invalid response
		req = requests.get(url,headers=headers)
	return req

def make_soup(markup):
	from bs4 import BeautifulSoup as soup
	return soup(markup,'html.parser')

def get_page_soup(url,headers={}):
	return make_soup(get_page(url,headers=headers).text)


def make_selenium_driver(headless=True,strategy='normal',timeout=2):
	from selenium import webdriver as wd
	opts = wd.firefox.options.Options();
	opts.page_load_strategy = strategy
	if headless: opts.headless = True
	# opts.add_argument("--headless") 		#works standalone
	driver=wd.Firefox(options=opts)
	# driver.set_page_load_timeout(2)	
	driver.implicitly_wait(10)	
	return driver 

def get_page_selenium(driver,url):
	try:
		driver.get(url)
		return driver.page_source
	except Exception as e:	
		print((e))

def push_tab(client,url):
	client.execute_script("window.open('{}', '_blank')".format(url))

def wlan_ip():
    import subprocess
    result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
    scan=0
    for i in result.split('\n'):
        if 'wireless' in i:
            scan=1
        if scan:
            if 'ipv4' in i:
                print (i.split(':')[1].strip())



class CONSTANTS:
	def get_ascii():
		r1=range(ord("0"),ord("9")+1)
		r2=range(ord("a"),ord("z")+1)
		r3=range(ord("A"),ord("Z")+1)
		enum=map(list, [r1,r2,r3])
		enum=[chr(el) for y in enum for el in y ]
		return enum



def randomstring(length):
	return "".join(random.choices(CONSTANTS.get_ascii() ,k=length))


#______________________________________________
#@#$%@#$%#$%#$%#+++CRYPTOGRAPHY+++#@$#@$#@$!@# 
class Swamicrypt:
	'''	
		usage : passwd=Swamicrypt('password')
		print(passwd.credentials)
	'''
	def __init__(self, basepassword,strength=4):
		self.strength=strength
		self.credentials= self.generate_key_and_lock(basepassword)
		self.key,self.enkrypted= (self.credentials)

	def generate_key_and_lock(self,basepassword):
		randlength=self.strength*len(basepassword)
		randstr=randomstring(randlength)
		ks_indices=[(i,v) for i,v in zip(range(randlength),randstr)]
		ks_indices=[poprandom(ks_indices) for k in basepassword]
		# ks_indices=random.sample([(i,v) for i,v in randstr] ,k=len(basepassword))
		ord_add=[ord(s)+ord(ki[1]) for s,ki in zip(basepassword,ks_indices)]
		key='.'.join([str(ki[0])+'+'+str(oa) for ki,oa in zip(ks_indices,ord_add)])
		return key,randstr

	def decryptx(self,keyPassTuple):
		key,enkrypted = keyPassTuple
		key=key.split('.')
		imods=[x.split('+') for x in key]
		orignalPassword=[ chr(int(x[1]) - ord(enkrypted[int(x[0])])) for x in imods ]
		return "".join(orignalPassword)

def hash(string):
	import hashlib
	return hashlib.md5(string.encode('utf-8')).hexdigest()

import time
def timeit(fn,*args,times=1000):
	ts=time.time()
	print(f'Running: {fn.__name__} | {times} Times')
	for x in range(times):
		fn(*args)
	te=time.time()
	print("T delta =",(te-ts)*1000,'ms')

def header_parser(firefoxAllHeaders):
	serializedHeaders=list((firefoxAllHeaders).values())[0]['headers']
	return { k:v for k,v in [x.values() for x in serializedHeaders] }

def cookie_parser():
	...


if __name__ == '__main__':
	# teachomatrixHeaders={"x-auth-token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoibmlraGlsIHN3YW1pIiwiZW1haWwiOiJuaWtoaWxzd2FtaTFAZ21haWwuY29tIiwiX2lkIjoiNjA0MzE2OTdmZDFjMTEwMDEzZjkwY2FhIiwidHlwZSI6IlMiLCJpYXQiOjE2MTU2Mjk5ODV9.gtsW-3SocTCVoquNhpZHs716mwmb6RircEZGKLDU1TI"}
	# urlEndpoint='https://teachomatrix.tk/api/quiz/605c66cc4be5d100138b7150/responses'
	# response=get_page(urlEndpoint,headers=teachomatrixHeaders).text
	# print((response))
	...
	x=Swamicrypt('somepassword')

	def testSwamicryptSpeed():
		x.decryptx(x.credentials)

	def testWebServerSpeed():
		requests.get('http://localhost:1111/')

	timeit(testWebServerSpeed,times=10)

	# print(x.decryptx(x.credentials))
		