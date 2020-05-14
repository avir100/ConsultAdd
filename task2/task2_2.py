'''
Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition 
If User Enter 2 - Subtraction
If User Enter 3 - Division
If USer Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
Ask user to enter two more numbers as first and second2 for calculating the average as soon as user choose an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time user can perform one action at a time.
'''
def secondinput(choice):
	while True:
		try:
			first, second = map(float, raw_input("Please enter 2 numbers seperated by a space \n").split())
			break
		except ValueError:
			print ("Invalid input, please try again \n")
	if choice == "1":
		return (first+second)
	if choice == "2":
		return (first-second)
	if choice == "3":
		return (first/second)
	if choice == "4":
		return (first*second)
	if choice == "5":
		return ((first+second)/2)

menu = {}
menu['1'] = "Addition" 
menu['2'] = "Subtraction"
menu['3'] = "Division"
menu['4'] = "Multiplication"
menu['5'] = "Average"
while True: 
	options = menu.keys()
	options.sort()
	print ("MENU:")
	for entry in options: 
		print entry, menu[entry]
	choice = raw_input("Please choose an option from the menu: \n") 
	if choice =='1':
		ans = secondinput(choice)
		if ans < 0:
			print ("NEGATIVE")		
		print (ans)
		break
	elif choice == '2': 
		ans = secondinput(choice)
		if ans < 0:
			print ("NEGATIVE")		
		print (ans)
		break
	elif choice == '3':
		ans = secondinput(choice)
		if ans < 0:
			print ("NEGATIVE")		
		print (ans)
		break
	elif choice == '4': 
		ans = secondinput(choice)
		if ans < 0:
			print ("NEGATIVE")		
		print (ans)
		break
	elif choice == '5': 
		ans = secondinput(choice)
		if ans < 0:
			print ("NEGATIVE")		
		print (ans)
		break
	else: 
		print "Invalid input, please try again" 