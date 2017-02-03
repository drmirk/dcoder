#python 3.4

def total_plays():
	'''
	given a number of participant, each participant plays one opponent 2 time, return total play
	'''
	user_inp = input()
	return int(user_inp) * (int(user_inp) -1)
	
print(total_plays())