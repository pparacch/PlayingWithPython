#Sorting Algorithms - Playing with sorting algorithms
#Python version 2.7

#SelectionSort algorithm
#Simple but inefficient algorithm
#asymptotic omplexity -> O(len(n)^2) - quadratic in the length of L

def selectionSort(L):
	"""Assume that L is a list of elements that can be compared using >.
	Sort L in ascending order."""
	len_L = len(L)
	no_of_steps = 0
	
	suffixStart = 0
	while suffixStart != len(L):
		no_of_steps +=1
		#Look at each element in suffix
		for i in range(suffixStart, len(L)):
			no_of_steps +=1
			if L[i] < L[suffixStart]:
				#Swap position of elements
				L[suffixStart], L[i] = L[i], L[suffixStart]
		suffixStart += 1
	print "Nuomber of elements (len(n)): %d, number of steps: %d" % (len_L, no_of_steps)


L = [1, 10, 2, 3, 5, 9, 8, 12, 11, 4, 6, 7]
print "Not sorted ->", L
selectionSort(L)
print "Sorted (selectionSort) ->", L
