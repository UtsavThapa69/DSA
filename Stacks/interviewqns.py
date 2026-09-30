#here i will use a list to create a stack
class Stack:
    def __init__(self):
        self.my_list = []

    def push(self, value):
        return self.my_list.append(value)

    def is_empty(self):
        return len(self.my_list) == 0

    def pop (self):
        if self.is_empty():
            return False
        return self.my_list.pop()

    def print_list(self):
        for  temp in range (len(self.my_list) - 1, -1, -1):
            print(self.my_list[temp])

    def peek(self):
        if self.is_empty():
            return False
        return self.my_list[-1]

    def size(self):
        return len(self.my_list)

def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed = ""
    while not stack.is_empty():
        reversed += stack.pop()

    return reversed

def parentheses(string):
    check = Stack()
    for char in string:
        if char == "(":
            check.push (1)

        else:
            if check.is_empty():
                return False
            check.pop()

    if check.is_empty() :
        return True
    return False

def sort_stack(stack):
    sorter = Stack()
    
    if stack.is_empty():
        return False

    while not stack.is_empty():
        temp = stack.pop()
        while not sorter.is_empty() and sorter.peek() > temp:
            stack.push(sorter.pop())

        sorter.push(temp)

    while not sorter.is_empty():
        stack.push(sorter.pop())

    return True

    

    
    

    
