'''
Write a program that accepts a string as an input from user and calculate the number of digits and letters.
     Expected output: consul12
     Letters 6
     Digits 2
'''
inputstring = str(raw_input("Please enter a string: \n"))
letters = 0
digits = 0
for x in inputstring:
	if x.isdigit():
		digits += 1
	elif x.isalpha():
		letters += 1

print "Digits: ", digits
print "Letters: ", letters
