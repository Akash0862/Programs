from que3 import generate_n_chars

def histogram(l):
	for x in l:
	 	char=generate_n_chars(x,'*')
	 	print(char)

histogram([3,6,5,4])