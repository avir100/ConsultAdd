'''
Write a program that prints all the numbers from 0 to 6 except 3 and 6.
       Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement
'''
count = 0
while count <= 6: #could also just to count<6 and remove 2nd condition in if statement below
	if count == 3 or count == 6:
		count += 1
		continue
	else:
		print (count), #using the comma enables us to get output in same line as
		count += 1
