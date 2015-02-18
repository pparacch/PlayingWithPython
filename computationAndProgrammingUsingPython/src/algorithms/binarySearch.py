#BinarySearch
#Asymptotic complexity: O(log(len(n)))
#Python version 2.7

#Suppose we know something about the order in which elemnets are stored
#e.g. a list of integer stored in ascending order.

def search(L, e):
	"""Assume that L is a list, elements ordered in ascending order
	Returns True if e is in L and False otherwise."""
	
	def bSearch(L, e, low, high):
		if high == low:
			return L[low] == e
		mid = (low + high) / 2
		if L[mid] == e:
			return True
		elif L[mid] > e:
			if low == mid: #Nothing left to search
				return False
			else:
				return bSearch(L, e, low, mid - 1)
		else:
			return bSearch(L, e, mid + 1, high)
	

	if len(L) == 0:
		return False
	else:
		return bSearch(L, e, 0, len(L) - 1)


print "Binary Search - 10000 elements - Worst case"
print search(range(10000), 10000)

print "Binary Search - 1 000 000 elements - Worst case"
print search(range(1000000), 1000000)

print "Binary Search - 100 000 000 elements - Worst case"
print search(range(100000000), 100000000)

print "Binary Search - 100 000 000 elements - looking for 99 111 999"
print search(range(100000000), 99111999)
