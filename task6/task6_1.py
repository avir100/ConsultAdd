#Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only higher order function.
def part1(n=[]):
	div7 = filter(lambda x : x % 7 == 0, n)
	out = filter(lambda x : x % 3 != 0, div7)
	print out

#Write a program in Python to  multiple the element of list by itself using traditional function and pass the function to map to complete the operation.
def part2(n=[]):
	out = map(lambda x : x * x, n)
	print out

#Write a program to Python find out the character in a string which is uppercase using list comprehension.
def part3(n=""):
	out = [i for i in n if i.isupper()]
	print out

#Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should maps the students with their respective subjects. Lets see how to do this using for loops and dictionary comprehension. 
def part4(student=['Smit', 'Jaya', 'Rayyan'], capital=['CSE', 'Networking', 'operating System']):
	out = (dict(zip(student,capital)))
	print out

#Learn more about yeild, next, generators
def part5():
	print ("Completed: Learn more about yeild, next, generators")

#Write a program in Python using generators to reverse the string.
def part6helper(s):
	for i in range(len(s)):
		yield s[len(s)-1-i]
def part6(s="Consultadd Training"):
	for i in part6helper(s):
		print (i),


#Decorator example
def part7helper_decorator(f):
	def wrapper():
		print ("Decorator output: We can do something before calling the function f()")
		f()
	return wrapper

def part7helper2():
	print ("Output from function 2")

def part7():
	b = part7helper_decorator(part7helper2)
	b()
part7()

'''
Learn about What is FRONT END and its Technologies and Tools
Make sure to mention at least 5 top notch technologies of Frontend.
Also mentioned the name of companies using those 5 technologies individually
'''
def part8():
	print "(i) \n", "5 frontend technologies --> ", "HTML5, Javascript, NodeJS, React, Bootstrap \n"
	menu = {}
	menu['HTML5'] = "Google play" #https://play.google.com/about/music/tour/
	menu['Javascript'] = "Paypal"
	menu['NodeJS'] = "Ebay"
	menu['React'] = "Airbnb"
	menu['Bootstrap'] = "Spotify"
	print "(ii) \n","Companies using the 5 technologies --> ", menu, "\n"
