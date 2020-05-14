import sys

#Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.
def part1():
	fourtypelist = ["hello", "world", 2, 4, 2.0, 2.7, 3.64, complex(3,2), "c", 0]
	print (typefourlist)

#Create a list of size 5 and execute the slicing structure
def part2():
	slicinglist = [1, 3, 4, 2, 11]
	print (slicinglist[1:3]) #output = 2,4

def inputlist_helper():
	inputlist = []
	size = 0
	count = 0
	while True:
		try:
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

#Create a list of given structure and run
def part3():
	l = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
	print "Access list [1, 2, 3, 4] --> \n", l[5][0:4]
	print ("***************************************")
	print "Access list [600,  700] --> \n", l[6:8]
	print ("***************************************")
	print "Access list [100, 300, 500, 600, 800] --> \n", l[0::2]
	print ("***************************************")
	print "Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]] --> \n", [l[::-1]]
	print ("***************************************")
	print "Access list [10] --> \n", [l[5][5][0]]
	print ("***************************************")
	print "Access list [ ] --> \n", []

#Create a list of thousand number using range and xrange and see the difference between each other. 
def part4():
	a = range(1000)
	b = xrange(1000)
	print ("Differences: \n")
	print "(1) Type \n", "range --> " + str(type(a)) + "\n", "xrange --> " + str(type(b)) + "\n"
	print "(2) Memory \n", "range --> " + str(sys.getsizeof(a)) + "\n", "xrange --> " + str(sys.getsizeof(b)) + "\n"
	print "(3) Slicing \n", "range --> can be sliced \n", "xrange --> cannot be sliced (TypeError) \n"
	print "(4) Runtime Speed \n", "range --> slower \n", "xrange --> faster \n"

#How Tuple is beneficial as compare to the list?
def part5():
	print "Tuples are immutable whereas lists are mutable. Tuples are faster than lists."

#Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.
def part6():
	l = range(1,100)
	for x in l:
		if x % 3 == 0 and x % 2 == 0:
			print (x),

#Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.
def part7():
	original = str(raw_input("Please input a string \n"))
	reverse = original[::-1]
	print "Reversed string --> ", reverse
	for x in range(len(reverse)):
		if reverse[x] in ('a', 'e', 'i', 'o', 'u'):
			print "index --> " + str(x),",", "vowel --> " + str(reverse[x])

#Write a program in Python to iterate through the string -hello my name is abcde- and print the string which has even length of word.
def part8():
	print ("I think this question is phrased incorrectly. The provided string will always have a fixed length. Did the question mean to ask to print the words with even length?")

#Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
def part9():
	l = inputlist_helper()
	target = 0
	while True:
		try:
			target = int(raw_input("Please enter target value\n"))
			break
		except ValueError:
			print ("Invalid input, please try again")
	print ("The following pairs sum to the desired target value:")
	for x in range(len(l)-1):
		for y in range(x+1,len(l)):
			if l[x] + l[y] == target:
				print l[x], l[y]

#Write a program in Python to complete the following task: [even odd question]
def part10():
	even_list = []
	odd_list = []
	indicator = ""
	totalsum = 0
	maxelem = 0
	while True:
		if len(even_list) == 5 or len(odd_list) == 5:
			break
		userinput = 0
		try:
			userinput = int(raw_input("Please enter int in range 1-50 \n"))
		except ValueError:
			print ("Invalid input, please try again")

		if userinput<=50 and userinput>=1:
			if userinput % 2 == 0:
				even_list.append(userinput)
			else:
				odd_list.append(userinput)
		else:
			print ("Input not in range, please try again")

	if len(even_list)==5:
		indicator = "even"
		totalsum = sum(even_list)
		maxelem = max(even_list)
	elif len(odd_list)==5:
		indicator = "odd"
		totalsum = sum(odd_list)
		maxelem = max(odd_list)

	print "Length of odd list: ", len(odd_list)
	print "Length of even list: ", len(even_list)
	print "Sum of " + indicator + "list: ", totalsum
	print "Max of " + indicator + "list: ", maxelem

#Write a program to find out the occurrence of a specific word from an alphanumeric statement.
def part11():
	userinput = raw_input("Please enter a string \n")
	out = {}
	for x in userinput:
		if x.isalpha():
			if x not in out.keys():
				out[x] = 1
			else:
				out[x] += 1
	for x in out.keys():
		print x, "=", out[x]

#Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
def part12():
	l = []
	original = (1,2,3,4,5,6,7,8,9,10)
	for x in range(len(original)):
		if original[x] % 2 == 0:
			l.append(original[x])
	print tuple(l)
