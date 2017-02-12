#python 3.4

def next_letter():
	'''
	a string is given, shift each letter of the string
	'''
	user_inp = input()
	changed_string = ''
	for i in user_inp:
		i = ord(i) + 1
		if(i == 91):
			i = 65
		if(i == 123):
			i = 97
		changed_string = changed_string + chr(i)
	return(changed_string)
	
print(next_letter())