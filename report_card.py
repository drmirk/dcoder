#python 3.4

def report_card():
	'''
	3 number is given, get average and return the grade
	'''
	user_inp = input()
	user_inp = user_inp.split(' ')
	sum = 0
	for i in user_inp:
		sum = sum + int(i)
	average = sum/3
	if(average > 90 and average <= 100):
		return 'A'
	elif(average > 80 and average <= 90):
		return 'B'
	elif(average > 70 and average <= 80):
		return 'C'
	elif(average > 60 and average <=70):
		return 'D'
	else:
		return 'F'
	
print(report_card())