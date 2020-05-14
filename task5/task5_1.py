import sys
import re
#Write a program in Python to allow the error of syntax to go in exception. 
def part1():
	try:
		eval("x===y")
	except SyntaxError as e: 
		print "Error: ", e

#Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode. 
def part2():
	f = sys.argv[1]
	while True:
		try:
			with open(f, 'r') as file:
				print (file.read())
			break
		except IOError as e:
			print "Error: ", e
			f = raw_input("The file name does not exist, please enter the file name again \n")

#Write a program to handle an error if the user entered the number more than four digits it should return -Please length is too short/long !!! Please provide only four digits 
class Error(Exception):
	pass

class ValueTooLargeError(Error):
	pass

def part3():
	while True:
		num = raw_input("Please enter the number (4 digits) \n")
		if len(num) <= 4:
			print ("Valid number")
			break
		else:
			raise ValueTooLargeError("Please length is too short/long !!! Please provide only four digits")

#Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
def part4():
	email = ""
	password = ""
	passverify = ""
	while True:
		email = raw_input("Please enter your user email \n")
		regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
		if (re.search(regex,email)):
			print ("Valid email")
			break
		else:
			print ("invalid email, please try again")

	while True:
		password = raw_input("Please enter password of length greater than 7 characters \n")
		if len(password) >= 7:
			break
		else:
			print ("Password too short, please try again")
	attempt = 0
	while attempt < 3:
		attempt += 1
		print "Attempt ", str(attempt), "/3"
		passverify = raw_input("Please re-type the password to verify \n")
		if passverify == password:
			print ("Your login was successful!")
			break
		else:
			if attempt == 3:
				print ("Your password did not match, you have reached the limit. Please try again later.")
			else:
				print ("Your password did not match, please try again.")


#https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and Raise concept.
def part5():
	print ("I have gone through the link - https://www.programiz.com/python-programming/exception-handling")

#Read any file using Python File handling concept and return only the even length string from the doc.txt file.
def part6():
	print ("I was confused by the wording of this question.")