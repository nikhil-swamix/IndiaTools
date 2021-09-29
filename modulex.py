##     ##  #######  ########  ##     ## ##       ######## ##     ## 
###   ### ##     ## ##     ## ##     ## ##       ##        ##   ##  
#### #### ##     ## ##     ## ##     ## ##       ##         ## ##   
## ### ## ##     ## ##     ## ##     ## ##       ######      ###    
##     ## ##     ## ##     ## ##     ## ##       ##         ## ##   
##     ## ##     ## ##     ## ##     ## ##       ##        ##   ##  
##     ##  #######  ########   #######  ######## ######## ##     ##
# ▀█████████▄  ▄██   ▄                                                                     
#   ███    ███ ███   ██▄                                                                   
#   ███    ███ ███▄▄▄███                                                                   
#_ ▄███▄▄▄██▀  ▀▀▀▀▀▀███                                                                   
# ▀▀███▀▀▀██▄  ▄██   ███                                                                   
#   ███    ██▄ ███   ███                                                                   
#   ███    ███ ███   ███                                                                   
# ▄█████████▀   ▀█████▀ 

# ███╗   ██╗██╗██╗  ██╗██╗  ██╗██╗██╗     
# ████╗  ██║██║██║ ██╔╝██║  ██║██║██║     
# ██╔██╗ ██║██║█████╔╝ ███████║██║██║     
# ██║╚██╗██║██║██╔═██╗ ██╔══██║██║██║     
# ██║ ╚████║██║██║  ██╗██║  ██║██║███████╗
# ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝                                        
# ███████╗██╗    ██╗ █████╗ ███╗   ███╗██╗
# ██╔════╝██║    ██║██╔══██╗████╗ ████║██║
# ███████╗██║ █╗ ██║███████║██╔████╔██║██║
# ╚════██║██║███╗██║██╔══██║██║╚██╔╝██║██║
# ███████║╚███╔███╔╝██║  ██║██║ ╚═╝ ██║██║
# ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝


import os, time
import random
import json
from pprint import pprint


import sys
if sys.executable.endswith('pypy3.exe'):
	pathlist=setload('python.paths')
	print(pathlist)
	sys.path.extend(pathlist)

# SET DATABASE ------------------
def setload(path,seperator='\n'): 
	rset=set(fread(path).split(seperator));
	rset.remove('') if '' in rset else ''
	return rset
def setwrite(path,setDataType): 
	fwrite(path,"\n".join(setDataType)+'\n')
def setupdate(path,newset):
	diff=newset - setload(path)
	if diff:
		fappend(path,'\n'.join(diff))
# SET DATABASE ------------------
def dictdifference(A,B): return dict(A.items() - B.items())

# FILES SYSTEM-------------------
def fread(path): f=open(path,'r+',encoding='utf-8').read() ;return f
def fwrite(fpath,content): f=open(fpath,"w+",errors="ignore") ;f.write(content)
def fappend(fname,content,suffix='\n'): f=open(fname,"a");f.write(content+suffix)
def touch(fpath,data=''):
	try: os.makedirs(os.path.split(fpath)[0],exist_ok=True)
	except: pass
	if not os.path.exists(fpath):
		fwrite(fpath,data)
		print('Touched',fpath)
def fdelta(path): return time.time()-os.path.getmtime(path)

#COUNTERS------------------------
def fincrement(cname,lock=''):
	c=int(fread(cname)); c+=1; fwrite(cname,str(c))

#JSON----------------------------
def jloads(string): return json.loads(string) #dict
def jload(path): 	return json.load(open(path)) #return dict
def jdumps(dictonary,indent=4): return json.dumps(dictonary,indent=indent) #return string
def jdump(dictonary,path): 	return json.dump(dictonary,open(path,"w+"),indent='\t') #write to disk
def jdumpline(dictonary,indent=None):return json.dumps(dictonary,indent=indent)
def jdumplines(dictionary,path): [fappend(path,jdumpline({k:dictionary[k]})) for k in dictionary]
def jloadlines(path):	
	jsonlines=open(path,'r').readlines()
	jldict={}
	for w in jsonlines:
		try: jldict.update(jloads(w))
		except: pass
	return jldict

def list_files_timesorted(folder):
	return [folder+x for x in os.listdir(folder)].sort(key=os.path.getmtime)

#TIMESTAMPERS---------------------
def datetime(filesafe=1):
	from datetime import datetime
	template='%Y%m%dT%H%M%S' if filesafe else '%Y-%m-%dT%H:%M:%S'
	return datetime.today().strftime(template)

def date():
	return datetime().split('T')[0]

def now():
	import time
	return int(time.time())

	

#RANDOMIZERS ---------------------
def shuffle(L): return [poprandom(L) for x in range(len(L))]
def randindex(L): return random.randrange(len(L)) # get random index
def poprandom(L):
	i = randindex(L) 
	L[i], L[-1] = L[-1], L[i] # swap with the last element
	return L.pop() # pop last element O(1)


#GENERATORS___________________________________
asciirange=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
def randomstring(length):
	lenascii=len(asciirange)
	r=[str(asciirange[random.randrange(lenascii)]) for x in range(length) ]
	return ''.join(r)

def hash(string): import hashlib; return hashlib.md5(string.encode('utf-8')).hexdigest()

#AUTO_PIP______________________________________
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
	proc=sp.run('pip list',stdout=sp.PIPE,stderr=sp.PIPE,text=1)
	if 'You should consider upgrading' in proc.stderr:
		upgradeCommand=proc.stderr.split('\'')
		sp.run(upgradeCommand[1])

	pipInstallSignal,pipUninstallSignal= 0,0 #declare signals as 0,
	satisfied={x:(x.lower() in proc.stdout.lower()) for x in modulesList} #list booleanization
	for k,v in satisfied.items():
		if not v:
			print(k,'is missing',end=' =|= ')
		# print(k+'\t:preinstalled')  else )
		if v==False: pipInstallSignal=1  
		if v==True: pipUninstallSignal=1 #NAND Condition if true then start uninstalling
	
	if mode=='download':
		proc=sp.run(f'pip download {" ".join(modulesList)} ' ,stdout=sp.PIPE	,shell=0)
		output=proc.stdout.read().decode('ascii').split('\n')
		print([x for x in output if 'Successfully' in x][0])
		proc.kill()
			
	if mode=='install': 
		if pipInstallSignal==True: 
			proc=sp.run(f'pip install {" ".join(modulesList)} -U'.format(),text=True,shell=1)
		else: print(f'{modulesList} were already installed'); return 1 

	if mode=='uninstall': 
		if pipUninstallSignal==True: 
			proc=sp.run(f'pip uninstall -y {" ".join(modulesList)}',text=True,shell=0)
		else: print(f'\n{modulesList} were already uninstalled'); return 1

	if proc.returncode==0:
		print('auto_pip Run Success')
		return proc.returncode

#SIMPLE-DB_________________________________
def hash_db(hashkey,*hashvalue,dirname='./LOCAL_DATABASE/'):
	''' 
	desc:
		creates a folder , and stores individual hashes as files.
		if : an index(hashkey) is given then check is file exists and open and return a dict{}
		else : if second argument (hashvalue[]) is given then create a dict
	'''
	itempath=dirname+hashkey
	if hashvalue:#write inputted value to memory
		fwrite(itempath,jdumps(hashvalue[0]))
	return jload(itempath)

#THREADING__________________________________
maxThreads=128
def apply_async(*args,):
	global POOL
	from concurrent.futures import ThreadPoolExecutor
	try:
		result=POOL.submit(*args,)
		return result
	except:
		POOL=ThreadPoolExecutor(maxThreads)
		result=POOL.submit(*args,)
		return result

#WEBFN______________________________________
def get_random_proxy():
	import re
	fname='proxylist.set'
	sourceurl='https://free-proxy-list.net/'
	cacheTime:'seconds'=30

	if os.path.exists(fname):
		tdelta=time.time() - os.path.getmtime(fname)
		if  tdelta>= cacheTime :
			pass
		else:
			print(f"LOG: using preexisting proxyDB: created {tdelta}s ago ")
			return setload(fname).pop()

	page=get_page(sourceurl)
	iplist=re.findall(r'[\d]+\.[\d]+\.[\d]+\.[\d]+:[\d]+',page.text)
	proxylist={'http://'+x for x in iplist}
	setwrite(fname,proxylist)
	print('LOG: refreshed proxy list')
	return proxylist.pop()



def make_session_pool(count=1): 
	return [requests.Session() for x in range(count)]

UserAgent={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
def get_page(url,headers={}): #return a page req object and retrive text later
	import requests
	headers.update(UserAgent)
	req=requests.get(url,headers=headers)
	return req

def post_page(url,data,headers={},):
	import requests
	r= requests.post(url,json=data,headers=headers)
	if not r:
		r= requests.post(url,data=data,headers=headers)

	return 


def make_soup(markup): 
	from bs4 import BeautifulSoup as soup
	try:
		return soup(markup,'lxml')
	except Exception as e:
		return soup(markup,'html.parser')
		

def get_page_soup(url,headers={}): 
	return make_soup(get_page(url,headers=headers).text)

def make_selenium_driver(headless=False,strategy='eager',timeout=10):
	from selenium import webdriver as wd
	opts = wd.firefox.options.Options();
	opts.page_load_strategy = strategy
	if headless: 
		opts.headless = True
	# opts.add_argument("--headless")
	driver=wd.Firefox(options=opts)
	driver.set_page_load_timeout(timeout)
	driver.implicitly_wait(10)	
	return driver 

def get_page_selenium(driver,url,new_tab=0,delay=2,waitcondition=lambda:True,waitcondition_polling=0.2,waitcondition_retries=10):
	try:
		if new_tab:
			driver.execute_script("window.open('{}', '_blank')".format(url))
		driver.get(url)

		while waitcondition()==False:
			if retry>=waitcondition_retries:
				break
			time.sleep(waitcondition_polling)

		return driver.page_source
	except Exception as e:	
		print(repr(e))

def parse_header(*firefoxAllHeaders,file=''):
	if firefoxAllHeaders: rawheader=firefoxAllHeaders[0] 
	if file: rawheader=jload(file)
	serializedHeaders=list((rawheader).values())[0]['headers']
	# print(serializedHeaders)
	return { k:v for k,v in [x.values() for x in serializedHeaders] }

def make_cookie(req):
	return ';'.join([f'{k}={v}' for k,v in req.cookies.items()])
	...

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

# Benchmarking _________________
def timeit(fn,*args,times=1000):
	import time
	ts=time.time()
	print(f'LOG: run {fn.__name__} X {times} Times')
	for x in range(times):
		fnoutput=fn(*args)
	tdelta=time.time() - ts
	print(f"LOG: Ttotal: {(tdelta)*1000}ms | time/call: {(tdelta/times)*1000}ms")
	print(f"LOG: output == ",fnoutput)
	return tdelta


class Tests:
	def testWebServerStress():
		def reqfn():
			d=requests.get(url2)
			print('fetch success',d.text)
		url1='http://swamix.com/'
		url2='http://swamix.com/api/news/tech'
		Parallelizer.tpoolexec(reqfn,threadCount=100)

def sync_pypy():
	import sys
	if sys.executable.endswith('python.exe'):
		pypypathsync=[x for x in sys.path]
		fwrite('python.paths','\n'.join(pypypathsync))


def get_nicehash_avg_payrate(myHashrate,size='10',algorithm='DAGGERHASHIMOTO'):
	from functools import reduce
	page=get_page(f'https://api2.nicehash.com/main/api/v2/hashpower/orderBook?size={size}&algorithm={algorithm}')
	daggerhashimoto_orderbook=page.json()
	data=daggerhashimoto_orderbook
	print(data)
	for region in data['stats']:
		for j in data['stats'][region]:
			regionOrderBook=data['stats'][region]['orders']
			if j == 'marketFactor':
				myMarketFactorSpeed=float(myHashrate)/float(data['stats'][region]['marketFactor'])
				# print(f"{myMarketFactorSpeed:.8f}")
			avgOrderValue=reduce(lambda x,y:x+y,[float(x['price']) for x in regionOrderBook])
		print("______________________",avgOrderValue/len(regionOrderBook))

#_________________________________________________
#                  _                       _      
#                 (_)                     | |     
#  _ __ ___   __ _ _ _ __     ___ ___   __| | ___ 
# | '_ ` _ \ / _` | | '_ \   / __/ _ \ / _` |/ _ \
# | | | | | | (_| | | | | | | (_| (_) | (_| |  __/
# |_| |_| |_|\__,_|_|_| |_|  \___\___/ \__,_|\___|
#_________________________________________________

# def binance_recent_trades():                                        
	# import pandas as pd
	# mktData=get_page('https://dapi.binance.com/dapi/v1/trades?symbol=ETHUSD_PERP').json()
	# dataframe=pd.DataFrame(mktData)[::-1]
	# for x in dataframe.iterrows():
	# 	print(x)

	# print(page.text)
	# print(dataframe.to_string())
	# print(dataframe.to_string())
	# for i in reversed(mktData):
		# print(f"{i['qty']:6}{i['price']}")
		# print(f"{i.items()}")

def google_enterprise_get_users_info(query):
	url=f'https://people-pa.clients6.google.com/v2/people/autocomplete?query={query}&client=GMAIL_WEB_DOMAIN&clientVersion.clientAgent=CONTACT_STORE&clientVersion.clientType=GMAIL_WEB_DOMAIN&clientVersion.clientVersion=contact_store_336195648&pageSize=300&key=AIzaSyBuUpn1wi2-0JpM3S-tq2csYx0z2_m_pqc&%24unique=gc606'
	page=requests.get(url,headers=parse_header(file='headers.json'))
	fwrite('response.txt',page.text)

if __name__ == '__main__':
	def has_page_changed(currentpage):
		global seleneum_lastpage
		try:
			if seleneum_lastpage:
				pass
		except:
			pass
# 90279d8e709cc88b2b918da5648c242055d4cab33e19bfe4583a00a9aeb9ace7
	# driver=make_selenium_driver()
	# url='https://medium.com/the-virago/are-men-biologically-hardwired-to-chase-after-much-younger-girls-66d4d428ee56'
	import requests,json
	url='https://www.quora.com/graphql/gql_para_POST?q=UserProfilePostsList_Posts_Query'
	postdata={"extensions": {"hash": "90279d8e709cc88b2b918da5648c242055d4cab33e19bfe4583a00a9aeb9ace7"}, "queryName": "UserProfilePostsList_Posts_Query", "variables": {"after": "17", "first": 3, "order": "most_recent", "uid": 1359639221 } }
	headers=UserAgent
	headers.update(parse_header(file='headers.json'))
	[print(h,':',v) for h,v in headers.items()]

	p=post_page(url,data=json.dumps(postdata),headers=headers)

	print(p,p.content)
	# r=get_page_selenium(driver,url,has_page_changed)
	# driver.close()





# html body div#root div.a.b.c div.s article.meteredContent div section.de.df.dg.dh.di