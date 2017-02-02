#python 3.4

def reverse_list():
	'''
	reverse a linked list, ends with -1
	'''
	user_inp = input()
	user_inp = user_inp[:-3]
	return user_inp[::-1]
	
print(reverse_list())