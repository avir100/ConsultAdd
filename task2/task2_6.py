from __future__ import print_function

'''
What is the output of the following code examples?
(i)   
   x=123 
   	   for i in x:
   		print(i)
(ii)
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(“error”)
(iii)
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break
'''
print ("(i)", "Type Error: Cannot iterate an integer value", sep="\n")
print ("***********************************************")
print ("(ii)", "0", "error", "1", "error", "2", sep="\n")
print ("***********************************************")
print ("(iii)", "1", "2", "3", "4", sep="\n")
print ("***********************************************")

