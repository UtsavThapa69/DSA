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
            
        
            
            
    
    