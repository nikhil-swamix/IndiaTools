PS C:\Users\dell\Documents\GitHub\modulex> .\pypy3\pypy3.exe .\benchmarks.py
arr+[a] 10.0M times             0.22965693473815918
arra[1]+1 10.0M times:          0.01772308349609375
s = assign 10.0M times:         0.002017974853515625
int assign 10.0M times:         0.008072137832641602
check a in b 10.0M times:       0.010123014450073242
extend int 10.0M times:         0.7274889945983887
>>>----->TOTAL TIME:			0.9950821399688721

___________________________________________________

<!-- ABOUT Key Checking methods -->
	def osexists(): os.path.exists('README.md')
	def dictexists(): 'apple' in d

LOG: run osexists X 10000 Times
LOG: Ttotal: 326.6410827636719ms | time/call: 0.03266410827636718ms
LOG: output ==  None
LOG: run dictexists X 10000 Times
LOG: Ttotal: 0.9992122650146484ms | time/call: 9.992122650146484e-05ms
LOG: output ==  None
osexists : dictexists = 326.8985922214269
___________________________________________________