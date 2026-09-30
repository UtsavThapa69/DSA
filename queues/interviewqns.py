#we need to prepare queues from stacks using lists only

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return True

    def dequeue(self):
        if not self.stack1:
            return None
        return self.stack1.pop()

    # but if the stack1 is not arranged as a proper queue

    # def dequeue(self):
    #     if not self.stack1:
    #         return None
    #     while len(self.stack1) != 1:
    #         self.stack2.append(self.stack1.pop())

    #     temp = self.stack1.pop()

    #     while self.stack2:
    #         self.stack1.append(self.stack2.pop())

    #     return temp
