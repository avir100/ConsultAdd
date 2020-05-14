from functools import reduce

#Write a program to reverse a string.
def part1(s=""):
	original = s
	if s == "":
		original = str(raw_input("Please input a string \n"))
	reverse = original[::-1]
	print "Reversed string --> ", reverse
	return reverse

#Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
def part2(s=""):
	original = s
	if s == "":
		original = str(raw_input("Please input a string \n"))

	upper = 0
	lower = 0
	print ('A'.isalpha())

	for x in original:
		if x.isalpha():
			if x.isupper():
				upper += 1
			elif x.islower():
				lower += 1

	print "No. of Upper case characters: ", upper
	print "No. of Lower case characters: ", lower
	return (upper,lower)

#Create a function that takes a list and returns a new list with unique elements of the first list.
def part3(l=[]):
	out = []
	original = l
	if l == []:
		original = raw_input("Please input the elements of the list seperated by a comma (ex - 2,4,1,4,7) \n").split(',')
	for x in original:
		if x not in out:
			out.append(x)
	print (out)
	return out

#Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def part4(s=""):
	original = s
	if s == "":
		original = str(raw_input("Please input a hyphen-separated sequence of words (ex: hello-my-name-is-abc)\n"))
	l = original.split('-')
	l.sort()
	out = ""
	for x in l:
		out = out + x + "-"
	out = out[0:len(original)]
	print out
	return out

#Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
def part5():
	totalinput = []
	print ("Please input a sequence of lines (submit input by pressing enter on an empty line) ")
	while True:
		l = raw_input()
		if l:
			totalinput.append(l)
		else:
			break
	userinput = "\n".join(totalinput)
	print (userinput.upper())

#Define a function that can receive two integral numbers in string form and compute their sum and print it in console.
def part6(s1="", s2=""):
	num1 = 0
	num2 = 0
	if s1 == "" or s2 == "":
		num1 = int(raw_input("Please enter the first integral number \n"))
		num2 = int(raw_input("Please enter the second integral number \n"))
	else:
		num1 = int(s1)
		num2 = int(s2)
	print "Sum: ", num1+num2

#Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
def part7(s1="", s2=""):
	st1 = ""
	st2 = ""
	if s1 == "" and s2 == "":
		st1 = raw_input("Please enter the first string \n")
		st2 = raw_input("Please enter the second string \n")
	else:
		st1 = s1
		st2 = s2

	if len(st1) == len(st2):
		print st1
		print st2
	elif len(st1) > len(st2):
		print st1
	else:
		print st2

# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.
def part8():
	l = []
	# assuming that between 1-20 does not include 20
	for i in range(1,20):
		l.append(i*i)
	print tuple(l)

#Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
# PART 9
def showNumbers(limit=-1):
	l = 0
	if limit == -1:
		while True:
			try:
				l = int(raw_input("Please input an int value for the limit \n"))
				break
			except ValueError:
				print ("Invalid input value, please try again")
	else:
		l = limit
	for x in range(l+1):
		if x % 2 == 0:
			print x, "EVEN"
		else:
			print x, "ODD"

#Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)
def part10():
	l = []
	for x in range(1,21):
		l.append(x)
	out = filter(lambda x: x % 2 == 0, l)
	return out
	print out

#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]
def part11():
	l = []
	for x in range(1,11):
		l.append(x)
	squared = map(lambda x: x * x, l)
	out = filter(lambda x: x % 2 == 0, squared)
	return out
	print out

# Write a function to compute 5/0 and use try/except to catch the exceptions
def part12():
	try:
		x = 5/0
	except Exception as e:
		print "Zero Division Error: ", e

#Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
def part13():
	original = [[1,2,3],[4,5],[6,7,8]]
	out1 = reduce(lambda x, y : x + y, original)
	print "For [[1,2,3],[4,5],[6,7,8]] --> ", out1
	out2 = reduce(lambda x, y : x + y, map(str, out1))
	print "For [1,2,3,4,5,6,7] --> ", out2

#What is the output of the following codes:
def part14():
	print "(i) The first function foo() returns value 2"
	print "(ii) The function f(x,4) is not defined and hence this line will throw an error. The error is not handled in the try-finally block. Therefore the output will be a NameError."






