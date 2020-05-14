'''
Write a program in Python which will find all such numbers which are divisible  by 7 but are not a multiple of 5, between 2000 and 3200.
'''
def method1():
	out = []
	start = 2000
	while start < 3200:
		if start % 7 == 0 and start % 5 != 0:
			out.append(start)
		start += 1

	for x in out:
		print (x)

def method2():
	start = 2000
	out = []
	while start < 3200:
		if start % 7 == 0 and start % 5 != 0:
			break
		else:
			start += 1

	while start < 3200:
		if start % 5 != 0:
			out.append(start)
		start += 7

	for x in out:
		print (x)

menu = {}
menu['1'] = "Solved using iterating over all integers (inefficient)" 
menu['2'] = "Solved using more efficient approach"

while True:
	options = menu.keys()
	options.sort()
	print ("MENU:")
	for entry in options: 
		print entry, menu[entry]
	choice = raw_input("Please choose an option from the menu: \n") 
	if choice =='1':
		method1()
		break
	elif choice == '2': 
		method2()
		break
	else:
		print ("Invalid input, please try again")