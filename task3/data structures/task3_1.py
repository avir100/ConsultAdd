import cmath
import numpy  


#Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
def part1():
	fourtypelist = ["hello", "world", 2, 4, 2.0, 2.7, 3.64, complex(3,2), "c", 0]
	print (typefourlist)

#Create a list of size 5 and execute the slicing structure
def part2():
	slicinglist = [1, 3, 4, 2, 11]
	print (slicinglist[1:3]) #output = 2,4


def inputlist_helper(number, flag):
	inputlist = []
	size = 0
	count = 0
	while True:
		try:
			if flag:
				if number == 1:
					size = int(raw_input("Please enter size of first input list \n"))
				elif number == 2:
					size = int(raw_input("Please enter size of second input list \n"))
			else:
				size = int(raw_input("Please enter size of the input list \n"))
			break
		except ValueError:
			print ("Invalid input, please try again")

	while count < size:
		while True:
			try:
				inputlist.append(int(raw_input("Please enter element " + str(count+1) + " of the desired list \n")))
				count += 1
				break
			except ValueError:
				print ("Invalid input, please try again")
	return inputlist

#Write  a program to get the sum and multiply of all the items in a given list.
def part3():
	l = inputlist_helper(1, False)
	print "Sum: ", sum(l)
	print "Product: ", numpy.prod(l)

#Find the largest and smallest number from a given list.
def part4():
	l = inputlist_helper(1, False)
	print "Smallest: ", min(l)
	print "Largest: ", max(l)

#Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 
def part5():
	l = inputlist_helper(1, False)
	out = []
	for x in l:
		if x % 2 != 0:
			out.append(x)
	print (out)

#Create a list of first and last 5 elements where the values are square of numbers between 1 and30 (both included).
def part6():
	bottom = 1
	top = 30
	out = []
	for x in range(5):
		out.append(bottom*bottom)
		out.append(top*top)
		bottom += 1
		top -= 1
	out.sort()
	print (out)

#Write a program to replace the last element in a list with another list.
def part7():
	l1 = inputlist_helper(1, True)
	l2 = inputlist_helper(2, True)
	userinput = [l1,l2]
	totallen = len(l1) + len(l2)
	counter = 0
	l1.pop()
	for x in l2:
		l1.append(x)
	print "User Input: ", userinput
	print "Answer: ", l1

#Create a new dictionary by concatenating the following two dictionaries:
def part8():
	a = {1:10, 2:20}
	b = {3:30, 4:40}
	out = a.copy()
	out.update(b)
	print (out)

#Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
def part9():
	n = 0
	while True:
		try:
			n = int(raw_input("Please enter the value of n (default value n=5) \n"))
			break
		except ValueError:
			print ("Invalid input, please try again")

	out = {}
	for i in range(1,n+1):
		out[i] = i*i
	print (out)

#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
def part10():
	seq = raw_input("Please enter a sequence of comma-separated numbers \n")
	l = seq.split(',')
	print "List --> ", l
	print "Tuple --> ", tuple(l)

