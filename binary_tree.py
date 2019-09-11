class node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.val)
        printinorder(root.right)

def printpreorder(root):
    if root:
        print(root.val)
        printpreorder(root.left)
        printpreorder(root.right)

def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.val)


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print("inorder traversal")
printinorder(root)

print("preorder traversal")
printpreorder(root)

print("postorder traversal")
printpostorder(root)
