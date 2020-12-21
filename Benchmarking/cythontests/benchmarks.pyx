cpdef int test():

	cdef str st='apple'
	cdef str chk='app'

	times=10*1000*1000
	for x in range(times):
		chk in st		
