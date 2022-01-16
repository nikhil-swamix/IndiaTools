import random

#______________________________________________
class Helpers:
	def get_ascii():
		r1=range(ord("0"),ord("9")+1)
		r2=range(ord("a"),ord("z")+1)
		r3=range(ord("A"),ord("Z")+1)
		enum=map(list, [r1,r2,r3])
		enum=[chr(el) for y in enum for el in y ]
		return enum

	def randindex(L):
		return random.randrange(len(L)) # get random index

	def poprandom(L):
		i = Helpers.randindex(L) 
		L[i], L[-1] = L[-1], L[i] # swap with the last element
		return L.pop() # pop last element O(1)

	def randomstring(length):
		return "".join(random.choices(Helpers.get_ascii() ,k=length))


#______________________________________________
def encryptx(basepassword,strength=4):
	randlength=strength*len(basepassword)
	randstr=Helpers.randomstring(randlength)
	ks_indices=[(i,v) for i,v in zip(range(randlength),randstr)]
	ks_indices=[Helpers.poprandom(ks_indices) for k in basepassword]
	ord_add=[ord(s)+ord(ki[1]) for s,ki in zip(basepassword,ks_indices)]
	key='.'.join([str(ki[0])+'+'+str(oa) for ki,oa in zip(ks_indices,ord_add)])
	return {'key':key,'randstr':randstr}

def decryptx(keypass):
	key,randstr = keypass['key'],keypass['randstr']
	key=key.split('.')
	imods=[x.split('+') for x in key]
	orignalPassword=[ chr(int(x[1]) - ord(randstr[int(x[0])])) for x in imods ]
	return "".join(orignalPassword)


p=encryptx('somepass')
print(p)
print(decryptx(p))