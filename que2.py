def overlapping(x1,x2):
	for item1 in x1:
		for item2 in x2:
			if item1==item2:
				return True
	else:
		return False
print(overlapping([1,2,3,4,5],[9,7,8,6,5]))