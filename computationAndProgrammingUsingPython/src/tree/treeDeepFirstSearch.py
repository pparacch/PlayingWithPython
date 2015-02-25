#Deep First Search for binary trees

def DFSBinary(root, searchFor):
	stack = [root]

	while len(stack) > 0:
	        print "Process: " + str(stack[0])
		if searchFor(stack[0]):
			return tracePath(stack[0])
		else:
			temp = stack.pop(0)
			
			if temp.getRightBranch():
				stack.insert(0, temp.getRightBranch())
			if temp.getLeftBranch():
				stack.insert(0, temp.getLeftBranch())
				
	return False


def tracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node] + tracePath(node.getParent())
        