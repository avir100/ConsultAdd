'''
Read the two parts of the question below: 
 Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 
Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
'''
from random import randint
answer = randint(1,10) #random number generated in range 1-10
print "Answer: ", answer

while True:
	try:
		number = int(raw_input("Guess the lucky number between 1-10: \n"))
		if (number == answer):
			print ("You guessed the correct number!")
			break
		else:
			while True:
				again = str(raw_input("Incorrect guess, would you like to guess again? \n"))
				if (again=='no'):
					print ("Program Stopped")
					break
				elif (again=='yes'):
					number = int(raw_input("Guess the lucky number between 1-10: \n"))
					if (number == answer):
						print ("You guessed the correct number!")
						break
				else:
					print ("Invalid input, please enter an integer value")
		break
	except ValueError:
		print ("Invalid input, please enter an integer value")


