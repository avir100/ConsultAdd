'''
Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “c” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.
'''
num = int(raw_input("Please enter a number \n"))
if num % 3 == 0 and num % 5 == 0:
	print ("Consultadd Python Training")
elif num % 3 == 0:
	print ("Consutadd")
elif num % 5 == 0:
	print ("c")