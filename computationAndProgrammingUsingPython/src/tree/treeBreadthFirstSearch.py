#Breatch First Search for binary trees
#Concept of Queue: FIFO - first in, first out

def BFSBinary(root, searchFor):
	queue = [root]

	while len(queue) > 0:
	        print "Process: " + str(queue[0])
		if searchFor(queue[0]):
			return True
		else:
			temp = queue.pop(0)
			
			#Remember first in - first out so 
			if temp.getLeftBranch():
				queue.append(temp.getLeftBranch())
			if temp.getRightBranch():
				queue.append(temp.getRightBranch())
				
	return False
