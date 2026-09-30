class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert1(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while temp:
            if new_node.value < temp.value:
                prev = temp
                temp = temp.left
                if temp is None:
                    prev.left = new_node
            elif new_node.value == temp.value:
                return False
            else:
                prev = temp
                temp = temp.right
                if temp is None:
                    prev.right = new_node

        return True

    def insert2(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        
        temp = self.root

        while True:
            if temp.value == value:
                return False
            elif temp.value < value:
                if temp.left is None:
                    temp.left = Node(value)
                    return True
                temp = temp.left
            else:
                if temp.value > value:
                    if temp.right is None:
                        temp.right = Node(value)
                        return True
                    temp = temp.right


    def contains(self, value):
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return False

            

        
