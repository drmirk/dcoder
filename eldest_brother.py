#python 3.4

def eldest_brother():
	'''
	find the eldest brother
	'''
	user_inp = input()
	user_inp = user_inp.split(' ')
	age_int = []
	for i in user_inp:
		age_int.append(int(i))
	return max(age_int)
	
print(eldest_brother())