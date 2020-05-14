import cmath
import sys
import functools

#Create three variables in a single line and assign different values to them and make sure their data types are invited different. Like one is int, another one is float and last one is string.
def part1():
	a,b,c = 1, "this variable type is string", 3.2
	print (type(a)) #int
	print (type(b)) #str
	print (type(c)) #float

#Create a variable of value type complex and swap it with another variable whose value is an integer.
def part2():
	com = complex(3,4)
	x = 1
	x, com = com, x
	print (x)
	print (com)

#Swap two numbers using third variable as result name and do the same task without using any third variable.
def part3():
	a = 1
	b = 2
	c = 1
	d = 2

	# using result variable
	result = a
	a = b
	b = result
	print ("Using result variable --> ", a, b, "\n")

	#without using result variable
	c, d = d, c
	print ("Without using result variable --> ", c, d, "\n")

#Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
def part4():
	userinput = raw_input("Please input a value \n")
	if sys.version_info[0] < 3:
		print ("Printing for python 2.x --> ", userinput)
	else:
		print ("Printing for python 3.x --> ", userinput)

'''
Write a program to complete the task given below:
Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable  call z.
Use z for adding 30 into it and print the final result by using variable result.
'''
def part5():
	while True:
		try:
			userinput1 = int(raw_input("Please enter first value between 1-10 \n"))
		except:
			print ("Invalid entry, please try again")
		else:
			if userinput1 <= 10 and userinput1 >= 1:
				break
			else:
				print ("Value out of range, please try again")
	while True:
		try:
			userinput2 = int(raw_input("Please enter second value between 1-10 \n"))
		except:
			print ("Invalid entry, please try again")
		else:
			if userinput2 <= 10 and userinput2 >= 1:
				break
			else:
				print ("Value out of range, please try again")
	z = userinput1 + userinput2
	result = z + 30
	print ("Result --> ", result)

# Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is : int/float/string/etc
def part6():
	a = raw_input("Please enter a value \n")
	type = "string"

	try:
		float(a)
		type = "float"
	except:
		pass

	try:
		int(a)
		type = "int"
	except:
		pass

	print ("The input value data type is: ", type)

#Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer:   https://capitalizemytitle.com/camel-case/)
def part7(s="consultadd test string"):
	l = s.split(" ")
	original = s
	lowercamel = l[0]
	snake = l[0].lower()
	for x in range(1, len(l)):
		lowercamel = lowercamel + l[x][0].upper() + l[x][1:len(l[x])]
		snake = snake + "_" + l[x].lower()
	uppercamel = lowercamel[0].upper() + lowercamel[1:len(lowercamel)]
	uppercase = lowercamel.upper()
	print ("Original string --> ", original)
	print ("Lower Camel --> ", lowercamel)
	print ("Upper Camel --> ", uppercamel)
	print ("Snake Case --> ", snake)
	print ("Upper Case --> ", uppercase)

#If one data type value is assigned to a variable and then a different data type value is assigned to a again. Will it change the value. If Yes then Why?
def part8():
	print ("Yes: The original value will be rewritten when a new value is assigned to variable a. Variable a will then return the newer assigned value.")

