#####################################################################
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
        no_of_steps += 1
        #Look at each element in suffix
        for i in range(suffixStart, len(L)):
            no_of_steps += 1
            if L[i] < L[suffixStart]:
                #Swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
    print "Number of elements (len(n)): %d, number of steps: %d" % (len_L, no_of_steps)
#####################################################################

#####################################################################
#MergeSort algorithm
#Introduce a divide-and-conquer approach. The basic dea is to combine
#solutions of simpler instances of teh original problem.

#merge -> asymptotic complexity is O(len(L))
#mergeSort -> asymptotic complexity is O(log2(len(L))) * O(len(L))
#O(log2(len(L))) is connected with the recursive algorithm.


noStepMergeSort = 0
noStepMerge = 0

def initializeCounter():
    global noStepMerge
    global noStepMergeSort

    noStepMerge = 0
    noStepMergeSort = 0


def merge(left, right, compare):
    """Assume left and right are sorted lists and compare (<)
    defines an ordering of the elements. Return a new sorted List (by compare)
    containing the same elements (left + right) would contain."""
    global noStepMerge

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        noStepMerge += 1
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        noStepMerge += 1
        result.append(left[i])
        i += 1

    while j < len(right):
        noStepMerge += 1
        result.append(right[j])
        j += 1

    return result

import operator


def mergeSort(L, compare=operator.lt):
    """Assume L is a List, and compare defines an ordering of the elements of L.
    Return a new sorted list containg the same elements as L. L is not modified."""

    global noStepMergeSort
    noStepMergeSort += 1

    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)


#####################################################################

L = [1, 10, 2, 3, 5, 9, 8, 12, 11, 4, 6, 7]
print "Not sorted ->", L
selectionSort(L)
print "Sorted (selectionSort) ->", L

print "\n--------------------------------\n"
initializeCounter()
L1 = [1, 10, 2, 3, 5, 9, 8, 12, 11, 4, 6, 7]
print "Len(): %d" % len(L1)
print "Not sorted ->", L1
sortedL1 = mergeSort(L1)
print "Sorted (mergeSort) ->", sortedL1
print "Total steps: %d, mergeSort steps: %d, merge steps: %d" % (noStepMerge + noStepMergeSort, noStepMergeSort, noStepMerge)