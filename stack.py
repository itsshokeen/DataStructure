class stack:

    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        return

    def pop(self):
        if len(self.stack)<1 :
            print("stack is empty")
            return
        else:
            return self.stack.pop()

    def size(self):
        length = len(self.stack)
        print(length)
        return


stack1 = stack()

stack1.push(12)
stack1.push(11)
stack1.push(13)
stack1.push(14)

stack1.size()
stack1.pop()
