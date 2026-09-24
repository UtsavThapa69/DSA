#i'll put my rough logic somewhere but i mostly just think in my head 
# so i may not upload
from basicqns import Node
# 1)palindrome
# 2)reverse 
# 3)partition list
# 4)swap pairs
# 5)reverse between
def palindrome(self):
    if self.head is None :
        return True
    if self.length == 1:
        return True

    left = self.head
    right = self.tail

    while left is not right and left.prev is not right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.prev

    return True

def reverse(self): 
    if self.head is None:
        return True 
    

    temp = None
    first = self.head

    while first:
        first.prev = first.next
        first.next = temp
        temp = first
        first = first.prev

    self.head , self.tail = self.tail , self.head

    return True

def partition_list(self, x):
    if self.head is None:
        return False
            
    d1 = Node(0)
    d2 = Node(0)
    lower = d1
    upper = d2
        
    current = self.head
  
    while current is not None:
        if current.value < x:
            current.prev = lower
            lower.next = current
            lower = current
            current = current.next
            lower.next = None
                
        else:
            current.prev = upper
            upper.next = current
            upper = current
            current = current.next
            upper.next = None
                
    lower.next = d2.next
    if d2.next is not None:
        d2.next.prev = lower

    self.head = d1.next   
    d1.next = None
    d2.next = None
    self.head.prev = None

    return True
            
        
def swap_pairs(self):
    if self.head is None or self.length == 1:
        return True

    d = Node(0)
    first = self.head
    second = first.next
    temp = d
    d.next = first
    first.prev = d

    while second:
        if second.next :
            second.next.prev = first

        first.next = second.next
        second.prev = temp
        temp.next = second
        first.prev = second
        second.next = first
        temp = first
        first = first.next
        if first is None:
            break
        second = first.next

    self.head = d.next
    d.next = None
    self.head.prev = None
    return True

def reverse_between(self, i , j):
    if i < 0 or j >= self.length:
        return False

    if i > j:
        return False

    d = Node(0)
    temp = d
    current = self.head
    d.next = self.head
    self.head.prev = d

    for _ in range (i):
        current = current.next
        temp = temp.next

    for _ in range(j - i):
        to_move = current.next
        current.next = to_move.next
        if to_move.next is not None:
            to_move.next.prev = current
        temp.next.prev = to_move
        to_move.next = temp.next
        to_move.prev = temp
        temp.next = to_move

    self.head = d.next
    d.next = None
    self.head.prev = None
    return True
        
