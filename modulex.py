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

def fwrite(fname,content):
	f=open(fname,"w+",errors="ignore")
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
#---------------------------


def list_files_by_time(folder):
	jobFileQueue=[folder+x for x in os.listdir(folder)]
	jobFileQueue.sort(key=os.path.getmtime)
	return (jobFileQueue)

def cleanup():
	import shutil
	try: shutil.rmtree('__pycache__')
	except :pass
# cleanup() 

#------------------IMPORT HELPER
def add_pwd_for_imports(pwf):
	import sys
	sys.path.append(os.path.dirname(pwf))

#------------------RANDOMIZERS
def randindex(L):
	return random.randrange(len(L)) # get random index

def pickrandom(L):
	i = randindex(L) 
	L[i], L[-1] = L[-1], L[i] # swap with the last element
	return L.pop() # pop last element O(1)

def shuffle(L):
	return [pickrandom(L) for x in range(len(L))]

# =============== AUTO_PACKAGE
def auto_pip(modulesList,mode='install'):
	'''
		+DOC: automatically Install Pip Packages Without Missing Module 
		Error before code runs and upgrades pip if its old, failsafe and fast
		can be invoked within code rather than running pip install blah 
		from cmd/terminal. mode can be +1 or -1, self explanatory.
		+USAGE: auto_pip('mode',[modules])
				auto_pip('install',['pytorch','numpy','etc...']) 
		where mode can be {install,uninstall,download} and modules is
		a standard py list ['numpy','pandas','tensorflow==1.15.1' and so on...]
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
		else: print(f'{modulesList} were already installed'); 
		proc.kill()
		return 1 

	if mode=='uninstall': 
		if pipUninstallSignal==True: 
			proc=sp.run('pip uninstall -y {}'.format(" ".join(modulesList)),text=True,shell=0)
		else: print(f'\n{modulesList} were already uninstalled'); return 1

	#CHECK SUCCESS OF PROCESS
	if proc.returncode==0:
		print('auto_pip Run Success')
		return proc.returncode




# =============== Miscalleneous
#CACHE--------------------------------------
class Cache: 
	pass#CREATES CACHE to save future calls cost






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





#=============== PARALLELISM

def asyncfn(fn, args):
	import threading
	x=threading.Thread(target=fn,args=args);x.start()
	return x




def parallelFunction(functionVariableName,threadCount):
	''' BEST USED FOR INTERNET ATTACKS OR REPETITIVE TASKS'''
	import threading
	pool=[]
	for i in range(threadCount):
		thread=threading.Thread(name='parallelFunction', target=functionVariableName)
		pool.append(thread)
		pool[i].start()





#===============WEB FUNCTIONS
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}

def make_session_pool():
	import requests
	return [requests.Session() for x in range(3)]


def get_page(url): #return a page req object and retrive text later
	import requests	
	req=requests.get(url,stream=True)
	if not req: #send headers only when invalid response
		req = requests.get(url,headers=headers)
	return req

def make_soup(markup):
	from bs4 import BeautifulSoup as soup
	return soup(markup,'html.parser')

def get_page_soup(url):
	return make_soup(get_page(url).text)

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
		return make_soup(markup)
	except Exception as e:	client.quit();	print("browser exit due to error"+str(e))

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
                return i.split(':')[1].strip()




#______________________________________________
#@#$%@#$%#$%#$%#+++CRYPTOGRAPHY+++#@$#@$#@$!@# 
class Swamicrypt:
	'''	usage : passwd=Swamicrypt('password')
		print(passwd.credentials)
	'''
	def __init__(self, basepassword):
		self.basepassword= basepassword
		self.credentials= self.make_key()
 
	def make_cryptspace(self):
		space=  [chr(x) for x in range(ord("0"),ord("9")+1)]
		space+= [chr(x) for x in range(ord("a"),ord("z")+1)]
		space+= [chr(x) for x in range(ord("A"),ord("Z")+1)]
		return space
 
	def cryptx(self,strength=4):
		keySpace="".join(random.choices(self.make_cryptspace() ,k=strength*len(self.basepassword)))
		return (keySpace)

	def make_key(self):
		stringx,keySpace=self.basepassword, self.cryptx(strength=4)
		ks_indices=random.sample(list(enumerate(keySpace)) ,k=len(stringx))
		ord_add=[ord(s)+ord(p[1]) for s,p in zip(stringx,ks_indices)]
		key=[str(ki[0])+'+'+str(oa) for ki,oa in zip(ks_indices,ord_add)]
		key='.'.join(key)
		return key,keySpace

	def decryptx(credentials):
		key,keyspace=credentials
		key=key.split('.')
		imods=[x.split('+') for x in key]
		orignalPassword=[ chr(int(x[1]) - ord(keyspace[int(x[0])])) for x in imods ]
		return "".join(orignalPassword)

if __name__ == '__main__':
	# print(f"hello {'anshil':10} poller podder yes papa")
	# L=['app','cas','sacas','asdas','asdwewe','3322dsds','vvxx']
	# print(shuffle(L))
	# url='https://www.mycryptopedia.com/crypto-trading-signals-an-ultimates-beginners-guide/?__cf_chl_captcha_tk__=76b71110f18b3829e833a42bed2e05eeb1be6ad4-1613428240-0-AdjBdGzKi81lzbixDDK5cHd7-ZF-HwwjQYo2-vqJ6gZAp3ltr-0GLclQ7Uy_H1EZqHNqScOpBRCtmJN7AfRVAtBGFBVX8Pm5zjq4ZWMInwryEuIpgYM_9zsN2dpus92sINzjgcRHC5tOUpNBpLYe4zOda1mfyfNQu-Df2Sn_rRKsESiOIOWaXoxic5qpDuQIdIDr76XwMpzc8yGVEz8Hjuj0bYgULPyPTY-IZpSxTw-HeK8h1vI4Bnc5Aj6l5YN4ARGqsYyXTj7oWiDR4MKx4lSZsDQwuxBxtV-sdYJRgPRB0EOQ5s3VYoKb7Lh36V1G6GqWTxDPKjc1eeps7nS3Y2O7SS6L6uyrAwRRgwJuUJrCE8eyLIrC7bnE9jVLHPWOov1vfKiX_rYtTHGtw4Wp-gZHgP5Uh2yEbzuTynYc6uZjLrIYp8osmdy3Mhz8dZYX4eVYUcxD3qWkUFY6g8Nwu9YwWoHZ4HqykG1xeNU_ey-ja9rv3f3XBrfulBBC1Mf4AwJgqMX5MejBmU9PB_gieDjL8yX8giRPUY5LQ5-k19-tgIOhAtQDJu0hyQNx7NaYz6IeXtvD6hIFWgvhQRbtKWU'
	# p=get_page_soup(url)
	# print(p)
	def dummy(x):
		print(x)

	data=[1,2,3,4,5,6,7,'asa','vv','r43v']
	multi_thread(dummy,data)