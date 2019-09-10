class queue:

    def __init__(self):
        self.queue = []

    def enqueue(self , data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue)<1:
            print("queue is empty")
            return
        else:
            self.queue.remove(0)

    def size(self):
        length = len(self.queue)
        print(length)
        return
