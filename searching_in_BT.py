class node:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key

def printlevelorder(root,value):
    if root is None:
        return
    queue = []
    queue.append(root)
    while (len(queue)>0):
            node = queue.pop(0)
            if value==node.data:
                print("value found")
            else:
                print("not found")
                return


            if node.left is not None:

                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

printlevelorder(root,6)
