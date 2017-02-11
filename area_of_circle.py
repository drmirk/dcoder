#python 3.4

def area_of_circle():
	'''
	radius is given, find the area of a circle,
	if radius negative return zero
	'''
	user_inp = float(input())
	if(user_inp <= 0):
		return 0
	else:
		PI = 3.14
		area = PI * (float(user_inp)**2.0)
		return('{0:.2f}'.format(area))
	
print(area_of_circle())