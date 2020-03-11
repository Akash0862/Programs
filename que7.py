
	
def find_longest_word(l):
	l1=[]
	for item in l:
		c=0
		for item2 in item:
			c+=1
		l1.append(c)
	for i in range(len(l1)):
		m=l1[i]
		for j in range(i+1,len(l1)):
			if m<l1[j] :
				m=l1[j]

		return m	
print(find_longest_word(['hello','this','is','my','answer']))