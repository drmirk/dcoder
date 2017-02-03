#python 3.4

def bit_flipper():
	'''
	a binary number is given, flip each bit
	'''
	user_inp = input()
	flipped_bit = ''
	for i in user_inp:
		if(i == '1'):
			flipped_bit = flipped_bit + '0'
		else:
			flipped_bit = flipped_bit + '1'
	return flipped_bit
	
print(bit_flipper())