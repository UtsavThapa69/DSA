class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        if self.first is None:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node

        else:
            temp = Node(value)
            self.last.next = temp
            self.last= temp

        self.length += 1
        return True
    def dequeue(self):
        if self.first is None:
            return False

        elif self.length == 1:
            temp = self.first
            self.first = None
            self.last = None
            self.length = 0
            return temp
               
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -=1
        return temp