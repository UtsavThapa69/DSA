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
    if self.head is None and self.length == 1:
        return True

    d = Node(0)
    current = self.head
    temp = d
    d.next = self.head
    self.head.prev = d

    
    