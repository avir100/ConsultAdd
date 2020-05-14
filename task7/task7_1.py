'''
Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
'''
def part1():
	c = 50
	h = 30
	while True:
		d = raw_input("Please input the elements of the list D seperated by a comma (ex - 2,4,1,4,7) \n").split(',')
		try:
			d_sanitized = [int(i) for i in d]
			break
		except ValueError as e:
			print ("Error: ", e)
			print ("Please try again")
	out = map(lambda x : (2*c*x)/h, d_sanitized)
	print (out)

#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have an area function which can print the area of the shape where Shapes area is 0 by default.
class Shape:
	def __init__(self):
		pass

	def area(self): #could also do def area(cls):
		return 0

class Square(Shape):
	def __init__(self, length): 
		self.length = length

	def area(self):
		return self.length * self.length

'''
 Create a class to find the three elements that sum to zero from a set of n real numbers.
Input array: [-25,-10,-7,-3,2,4,8,10]
Output: [[-10,2,8],[-7,-3,10]]
'''
class part3:
	def __init__(self, inputlist = [-25,-10,-7,-3,2,4,8,10]):
		self.inputlist = inputlist

	def threesum(self):
		out = []
		for x in range(len(self.inputlist) - 2):
			for y in range(x + 1, len(self.inputlist) - 1):
				for z in range(y + 1, len(self.inputlist)):
					if self.inputlist[x] + self.inputlist[y] + self.inputlist[z] == 0:
						out.append([self.inputlist[x], self.inputlist[y], self.inputlist[z]])
		print (out)
		return out

#What is the output of the following code?
def part4():
	print ("(i) Done for us \n")
	print ("(ii) \n", "Output --> 1 2 \n", "Reason --> when main() is called, obj of der class is created which also inherits properties of class A. \n")
	print ("(iii) \n", "Output --> 3 1 \n", "Reason --> when main() is called, obj of B class is created. The initial attributes of this object are assigned as x=3 y=0. This is because the x attribute is set since the parent constructor is called from the constructor of class B. Finally when the count() function is called, the y value is incremented. \n")
	print ("(iv) \n", "Output --> 30 \n", "Reason --> when obj is created as an instance of class B, the parent constructor is used to instantiate the object. According to the parent conductor, the multiply() function is called. This function exists for the parent and chill class. According to the hiarachy of priority, the child multiply() funciton is used. \n")
part4()
'''
Create a Time class and initialize it with hours and minutes.
Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Make a method displayTime which should print the time.
Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
'''
class Time:
	def __init__(self, hours, minutes):
		if minutes >= 60:
			self.hours = hours + 1
			self.minutes = minutes - 60
		else:
			self.hours = hours
			self.minutes = minutes

	def addTime(t1, t2):
		return  Time(t1.hours + t2.hours, t1.minutes + t2.minutes)

	def displayTime(self):
		print (self.hours, " hours and ", self.minutes, " minutes")

	def DisplayMinute(self):
		total = (self.hours * 60) + self.minutes
		print (total, " minutes")

def part5():
	a = Time(2,50)
	b = Time(1,20)
	c = Time.addTime(a,b)
	c.displayTime()
	c.DisplayMinute()


'''
   Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:
	- yearPasses() should increase the  instance variable by .
	- amIOld() should perform the following conditional actions:
		If , print You are young..
		If  and , print You are a teenager..
		Otherwise, print You are old..	
'''
class Person:
	def __init__(self, n):
		if n < 0:
			print ("Age is not valid, setting age to 0")
			self.age = 0
		else:
			self.age = n

	def yearPasses():
		print ("Question is incomplete")
		pass

	def amIOld():
		print ("Question is incomplete")
		pass
