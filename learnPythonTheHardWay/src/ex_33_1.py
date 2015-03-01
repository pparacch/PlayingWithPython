#While loops
#When using this type of loop be careful - the condition that you are testing will become False
#at some point.

def createIntegerListTil(max, step = 1):
	i = 0
	elements = []

	while i < max:
		elements.append(i)
		i += step
	
	return elements


numbers = createIntegerListTil(6) #no step provided - default value is useid
print "Numbers: ", numbers

for num in numbers:
	print num

numbers = createIntegerListTil(25, 2)
print "Numbers: ", numbers

for num in numbers:
	print num


