def max_in_list(l):
	
	for i in range(len(l)):
		m=l[i]
		for j in range(i+1,len(l)):
			if m<l[j] :
				m=l[j]

		return m	
print(max_in_list([10,71,1,2,76,3,4,7,6,76,89,2,1,0,101]))
