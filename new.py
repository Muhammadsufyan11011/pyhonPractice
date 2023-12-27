def shout():
	return 'source code'.upper()

def whisper():
	return 'Source Code'.lower()

def display(func):
	print(func())

# display(shout)

# display(whisper)


def get_age_in_month(age):
	def show(): 
		print('i am an inner func')

	return show

get_age_in_month(25)()