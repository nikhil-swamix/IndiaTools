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
def touch(fpath):
	head=os.path.split(fpath)[0]
	try: 
		os.makedirs(head,exist_ok=True)
	except:
		pass
	if not os.path.exists(fpath):
		open(fpath,"w+",errors="ignore").close()
		print('Touched',fpath)
def ftdelta(path): return os.path.getmtime()

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

def fmdelta(path):#fmdelta=file mod delta
	os.path.getmtime
	

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

def get_page(url,headers={}): #return a page req object and retrive text later
	import requests
	# UserAgent={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 Instagram 12.0.0.16.90 (iPhone9,4; iOS 10_3_3; en_US; en-US; scale=2.61; gamut=wide; 1080x1920)'}

	UserAgent={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
	headers.update(UserAgent)
	req=requests.get(url,headers=headers)
	return req

def make_soup(markup): 
	from bs4 import BeautifulSoup as soup
	try:
		return soup(markup,'lxml')
	except Exception as e:
		return soup(markup,'html.parser')
		

def get_page_soup(url,headers={}): 
	return make_soup(get_page(url,headers=headers).text)

def make_selenium_driver(headless=True,strategy='normal',timeout=5):
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

def get_page_selenium(driver,url,new_tab=0):
	try:
		if new_tab:
			driver.execute_script("window.open('{}', '_blank')".format(url))

		driver.get(url)
		return driver.page_source
	except Exception as e:	
		print((e))

def parse_header(firefoxAllHeaders):
	serializedHeaders=list((firefoxAllHeaders).values())[0]['headers']
	return { k:v for k,v in [x.values() for x in serializedHeaders] }

def parse_cookie():
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
                                        

if __name__ == '__main__':
	# url='https://www.teachthought.com/post-sitemap1.xml'	
	# links=set(x.text for x in get_page_soup(url).select('loc'))
	# print(links)
	import urllib.request
	...

	headers={
	"Request Headers (2.578 KB)": {
		"headers": [
			{
				"name": "Accept",
				"value": "application/vnd.linkedin.normalized+json+2.1"
			},
			{
				"name": "Accept-Encoding",
				"value": "gzip, deflate, br"
			},
			{
				"name": "Accept-Language",
				"value": "en-US,en;q=0.5"
			},
			{
				"name": "Connection",
				"value": "keep-alive"
			},
			{
				"name": "Content-Length",
				"value": "234"
			},
			{
				"name": "content-type",
				"value": "application/json; charset=utf-8"
			},
			{
				"name": "Cookie",
				"value": "JSESSIONID=\"ajax:0343548922120190385\"; lang=v=2&lang=en-us; bcookie=\"v=2&9dfa01b2-15c1-4571-82c4-1862cbdbcfb2\"; bscookie=\"v=1&20210822042254c751b295-5c36-402b-8073-b0c08e80ac1aAQH8qNbN6o8XRZbil8KJ6rF0C1ea3j52\"; lidc=\"b=TB21:s=T:r=T:a=T:p=T:g=3931:u=1:x=1:i=1629666702:t=1629690501:v=2:sig=AQHFFxxsX3n6U4vUMs97WZDnwRB9xmm0\"; G_ENABLED_IDPS=google; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C18862%7CMCMID%7C61970616575596095545501808405828739855%7CMCOPTOUT-1629673761s%7CNONE%7CvVersion%7C5.1.1; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; liap=true; li_at=AQEDATdACk0FsEKYAAABe2wY6ukAAAF7kCVu6U4ABYwOTG2N5fA7sBMWN2xuIMCcGCSezmmEzTIOXXdnYlVVYg01Z0B4S2jWnbVnd6GyIOY0HiYRT6_WEzznSAazH6RmWLTJrM09lyq9BYE-qBdBeL09; timezone=Asia/Kolkata; _ga=GA1.2.695336261.1629606188; _gid=GA1.2.1237390366.1629606188; UserMatchHistory=AQKx3-axrpsKOAAAAXtvtG5Y2vk06iVwOv4SU_twLlFf3WcSAWUac39buFjbfAL3f6ewc1AQwD3cwIJ4QZ5G4LRLsgvZdHPMIOkTAuLGPwXxUcNLF3-5P0m6fA7A_eSscOYCi_-QaYEbL2C39UGFqok8TFj556zbnKnkChSr3OM7AqXvtcmgFg57E5v4j9TCIEsHPYQ9unlYXXUuoJ8Ej9jsECgCpe1TcjJYpZNGOc4nRCH42zPNXGbjBK9hVvttGX2Zzv8T4ri41cKSl_erAZY1OJ2EX9IqBZ-5ynw; li_sugr=952abf89-9926-42f4-b623-a3383d9ae223; _guid=722786b6-14cc-4de7-bb19-f774555fa263; AnalyticsSyncHistory=AQIQ1d-04lSKtwAAAXtsGRTyXYzkaB3tG5E9Ta_im8-pQeq92VNcLFTZ--4yZFC4uBqQIzrAHhMlOFEGvfjclA; lms_ads=AQGMFZx2JdQATQAAAXtsGRZHGcUhtf-QZ547pfMhpOg9_d41ZAfgeA63jpqA345RS_IgEK16q_DqwtyT6w7G2Z3AnP2jd-Y4; lms_analytics=AQGMFZx2JdQATQAAAXtsGRZHGcUhtf-QZ547pfMhpOg9_d41ZAfgeA63jpqA345RS_IgEK16q_DqwtyT6w7G2Z3AnP2jd-Y4; _gcl_au=1.1.748534523.1629606191; _gat=1"
			},
			{
				"name": "csrf-token",
				"value": "ajax:0343548922120190385"
			},
			{
				"name": "DNT",
				"value": "1"
			},
			{
				"name": "Host",
				"value": "www.linkedin.com"
			},
			{
				"name": "Origin",
				"value": "https://www.linkedin.com"
			},
			{
				"name": "Referer",
				"value": "https://www.linkedin.com/in/manjusha-behara-669480b2/"
			},
			{
				"name": "Sec-Fetch-Dest",
				"value": "empty"
			},
			{
				"name": "Sec-Fetch-Mode",
				"value": "cors"
			},
			{
				"name": "Sec-Fetch-Site",
				"value": "same-origin"
			},
			{
				"name": "TE",
				"value": "trailers"
			},
			{
				"name": "User-Agent",
				"value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
			},
			{
				"name": "x-li-lang",
				"value": "en_US"
			},
			{
				"name": "x-li-page-instance",
				"value": "urn:li:page:d_flagship3_profile_view_base;6yDsuv4GRmyc2igds2qAww=="
			},
			{
				"name": "x-li-track",
				"value": "{\"clientVersion\":\"1.9.1883\",\"mpVersion\":\"1.9.1883\",\"osName\":\"web\",\"timezoneOffset\":5.5,\"timezone\":\"Asia/Kolkata\",\"deviceFormFactor\":\"DESKTOP\",\"mpName\":\"voyager-web\",\"displayDensity\":0.8955223880597015,\"displayWidth\":1279.7014925373135,\"displayHeight\":720}"
			},
			{
				"name": "x-restli-protocol-version",
				"value": "2.0.0"
			}
		]
	}
	}

	postdata={
	"invitation": {
		"emberEntityName": "growth/invitation/norm-invitation",
		"invitee": {
			"com.linkedin.voyager.growth.invitation.InviteeProfile": {
				"profileId": "ACoAABfrG7EB0ikQuph_TebLIQrePDEl4BTQZx8"
			}
		},
		"trackingId": "XE/jcWHmTlq5Yy/vsli5GQ=="
	}
	}

	url='https://www.linkedin.com/in/manjusha-behara-669480b2/'

	print(get_page_soup(url,postdata))

