#Linear Search Algorithm
#Asymptotic Complexity: O(len(L))
#Python version 2.7

#Main points: Linear Search and indirection to access elements
#Indirection: in Python a list is represented as a lenght (the no ofobjects in teh list) and a sequence of fixed-size pointers (to the actual elements)

#Linear search -> looping through all of the elements of the list till I find the one, and return True. Otherwise return False.
#This is the best thing that we can do when we know nothing about the relationship of the values of the elements in teh list and the order they are stored.

#Worst Case Scenario: element is not present in the list
#Best Case Scenario: list is emty

def search(L, e):
	for i in range(len(L)):
		if i == e:
			return True
	return False




print "Linear Search for 100 elements - WorstCase ..."
print search(range(100), 100)

print "Linear Search for 1000 elements - WorstCase ..."
print search(range(1000), 1000)

print "Linear Search for 10000 elements - WorstCase ..."
print search(range(10000), 10000)

print "Linear Search for 10 000 000 elements - WorstCase"
print search(range(10000000), 10000000)


#What if we know something about the order of the elements - e.g elements have been stored in ascending order
#Improved Linear Search

def search_improved(L, e):
	"""Assume L is a List, teh elemets in teh list are ordered in ascending order.
	Return True if e is in L and False otherwise."""

	for i in range(len(L)):
		if L[i] == e:
			return True
		if L[i] > e:
			return False
	return False

print "Improved - assumption elements are ordered in ascending order"
print "Linear Search for 200 elements - WorstCase ..."
print search_improved(range(0, 200, 2),300)

print "Linear Search for 2000 elements - WorstCase ..."
print search_improved(range(0, 2000, 2), 3000)

print "Linear Search for 20000 elements - Element missing but now worst case ..."
print search_improved(range(0, 20000, 2), 9555)

print "Linear Search for 20 000 000 elements - Element is missing but not worst case ..."
print search_improved(range(0, 20000000,2), 10000001)



 
