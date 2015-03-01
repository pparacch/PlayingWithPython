#While loops
#When using this type of loop be careful - the condition that you are testing will become False
#at some point.

i = 0
numbers = [] #an empty list

while i < 6: #this is my exit condition when will become False
	print "At the top i is %d" % i
	numbers.append(i) #add i at the end of the list

	i += 1 #Increment i in order to "trigger" the exit condition
	print "Numbers now (after adding i): " , numbers
	print "At the bottom i is %d" % i

print "Numbers: ", numbers

for num in numbers:
	print num


