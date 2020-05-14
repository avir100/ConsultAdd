from random import randint

'''
In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.
'''

counter = 1
answer = randint(1,10)
print "Answer: ", answer

while counter <= 5:
	number = int(raw_input("Guess the lucky number between 1-10: \n"))
	if (number == answer):
		print ("Good guess!")
		break
	else:
		if counter == 5:
			print ("Sorry but that was not very successful")
		else: 
			print ("Try again!")
	counter += 1
