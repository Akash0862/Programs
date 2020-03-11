def length_of_words(l):
	l1=[]
	for item in l:
		c=0
		for item2 in item:
			c+=1
		l1.append(c)
	return l1
print(length_of_words(['hello','this','is','my','answer']))