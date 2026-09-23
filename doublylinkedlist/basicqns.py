class Node:
    def __init__ (self, value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:

    def __init__(self, value):
        new_node=Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append (self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

        return True

    def prepend (self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else :
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

        return True

    def pop(self):
        if self.head is None:
            return None

        if self.length == 1:
            temp = self.head 
            self.head = None 
            self.tail = None 
            self.length = 0
            return temp

        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None 
        self.length -= 1
        return temp

    def pop_first(self):
        if self.head is None:
            return None

        if self.length == 1:
            temp = self.head 
            self.head = None 
            self.tail = None 
            self.length = 0
            return temp

        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        last = self.tail

        if (self.length // 2) > index:
            for _ in range(index) :
                temp = temp.next

            return temp

        else:
            for _ in range(self.length - 1 - index):
                last = last.prev

            return last

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False

        temp = self.get(index)
        new_node = Node(value)

        temp.value = new_node.value
        return True

    def insert (self, index, value):
        if index < 0 or index > self.length:
            return False

        new_node = Node (value)

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        temp = self.get(index - 1)

        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index >= self.length or index < 0:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        
        temp = self.get(index)
        before = temp.prev
        after = temp.next

        before.next = after
        after.prev = before
        temp.prev = temp.next = None
        self.length -= 1
        return temp

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next