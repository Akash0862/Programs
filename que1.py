def is_member(x,args):
	if x in args:
		return True
	else:
		return False
print(is_member(6,[1,2,3,4,5]))
print(is_member("e", ['a', 'e', 'i', 'o', 'u']))
print(is_member(19, [1,3,4,6,18,20]))
print(is_member('abc', ['abc', ' pqr', 'rty', 'poihvg']))
print(is_member('panda', ['lion', 'zebra', 'elephant', 'panda']))