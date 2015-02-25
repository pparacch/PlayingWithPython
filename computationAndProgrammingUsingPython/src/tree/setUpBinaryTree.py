import BinaryNode

n5 = BinaryNode.binaryTree(5)
n2 = BinaryNode.binaryTree(2)
n1 = BinaryNode.binaryTree(1)
n4 = BinaryNode.binaryTree(4)
n8 = BinaryNode.binaryTree(8)
n6 = BinaryNode.binaryTree(6)
n7 = BinaryNode.binaryTree(7)
n3 = BinaryNode.binaryTree(3)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
##[n2] n5 [n8]


n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
##[n1] n2 [n4]

n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
##[n6] n8 [n7]

n4.setLeftBranch(n3)
n3.setParent(n4)
##[n3] n4 []

def find6(node):
    return node.getValue() == 6

def find10(node):
    return node.getValue() == 10

def find2(node):
    return node.getValue() == 2