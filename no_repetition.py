#python 3.4

def no_repetition():
	'''
	remove repeated letter from string
	'''
	user_inp = input()
	new_str = ''
	for i in user_inp:
		if(i not in new_str):
			new_str += i
	return new_str
	
print(no_repetition())