from random import randint

'''
Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
           		counter=1
		While counter <= 5:
			print(“Type in the”, counter, “number”
			counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
'''
counter = 1
answer = randint(1,10)
print "Answer: ", answer

while counter <= 5:
	number = int(raw_input("Guess the lucky number between 1-10: \n"))
	if (number == answer):
		print ("Good guess!")
	else:
		if counter == 5:
			print ("Game over!")
		else: 
			print ("Try again!")
	counter += 1
