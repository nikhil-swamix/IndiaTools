import time
times=100*1000*1000

tot=time.time()
s=time.time()

# for i in range(times):
# 	barray=[1,2,3]
# 	barray+[1]
# print(f'{"arr+[a] {0}M times"		:30}'.format(times/1000000),time.time()-s)

s=time.time(); 
barray=[1,2,3]
for i in range(times): barray[1]=barray[1]+1
print(f'{"arra[1]+1 {0}M times:"	:30}'.format(times/1000000),time.time()-s)

# s=time.time()
# for i in range(times): a='1123123213213asds1'
# print(f'{"s = assign {0}M times:"	:30}'.format(times/1000000),time.time()-s)

# s=time.time()
# for i in range(times): a=1123123213213123231
# print(f'{"int assign {0}M times:"	:30}'.format(times/1000000),time.time()-s)

# s=time.time()
# for i in range(times): 'anshul' in 'anshual'*100+'anshul'
# print(f'{"check a in b {0}M times:"	:30}'.format(times/1000000),time.time()-s)

# s=time.time()
# a=[1]
# for i in range(times): a.extend((10,20))
# print(f'{"extend int {0}M times:"	:30}'.format(times/1000000),time.time()-s)


print('>>>----->TOTAL TIME:			  ',time.time()-tot,'\n')



# print(string)