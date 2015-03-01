#Loops & Lists
#for loops using the elements of a list

the_count = [1, 2, 3, 4, 5] # a list of integers
fruits = ["apples", "oranges", "pears", "apricots"] # a list of strings
change = [1, "pennies", 2, "dimes", 3, "quarters"] # a mixed list (integers & strings)

##This is how we can access the elements in a list
##looping through teh content of the list

#loop through the elements of a list
for item in the_count:
	# use %d cause we know that the list contains integers
	print "This is count %d" % item

#loop again
for fruit in fruits:
	# use %s cause we know the list contains strings
	print "A fruit of type: %s" % fruit

#and again
for item in change:
	# use %r cause we do not know the type of the element in the list
	print "I got %r" % item

##We can also build a list - starting withan empty list
elements = [] #this is an empty list

for i in range(1, 6): #list of 1,2,3,4,5
	print "Adding %d to the list." % i
	elements.append(i) #add i as an element at the end of the list

#And now we can print out the element in the list
for element in elements:
	print "Element %d" %  element

##We can create mutidimensional lists
anotherList = [[1,2,3], [4,5,6], [7,8,9]]

for element in anotherList:
	print "I got %r" % element
	#Accessing the inner elemets

	for elmt in element:
		print "    >>>> element %d" % elmt




