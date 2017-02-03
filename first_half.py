#python 3.4

def first_half():
	'''
	first half of a string
	'''
	user_inp = input()
	half = len(user_inp) / 2
	return user_inp[:int(half)]
	
print(first_half())