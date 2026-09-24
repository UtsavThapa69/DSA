class Node:
    def __init__(self, value):
        self.value = value
        #self.down = None: this was the one that i wanted to put here
        # but the convention is necessary
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.height = 1
            return True
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return False
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    