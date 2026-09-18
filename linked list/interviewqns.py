#i will also put the logic in a note or somewhere later
#the constraint is that we cant use or find self.length

#finding middle node
from basic import Node
def middle_node(self):
    if self.length==0:
        return False
    fast=slow=self.head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow

#has loop

def has_loop(self):
    if self.head is None:
        return None
    fast=slow=self.head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast is slow:
            return slow
    return None

#kth node from end
#i am not doing any error handling
def from_end(self,k):
    slow=fast=self.head
    for _ in range(k):
        if fast is None:
            return None
        fast=fast.next

    while fast:
        slow=slow.next
        fast=fast.next
    return slow

#in a linked list like 1-2-3-1-3-2
def find_duplicates(self):
    if self.head is None:
        return False
    current=self.head
    while current:
        runner=current
        while runner.next:
            if runner.next.value==current.value:
                runner.next=runner.next.next
            else:
                runner=runner.next
        current=current.next
    return True

#converting binary to decimals
#the user can go to hell if he puts something else than a binary number in the LL🙂‍↕️
def binarytodecimal(self):
    if self.head is None:
        return None
    
    current=self.head
    sum=current.value
    while current.next:
        current=current.next
        sum=current.value + (2 * sum)

    return sum
#harder problems
def partition_value(self,x):
    if self.head is None:
        return False

    d1=Node(0)
    d2=Node(0)
    prev1=d1
    prev2=d2
    while self.head:
        if self.head.value<x:
            prev1.next=self.head
            prev1=prev1.next
            self.head=self.head.next
            prev1.next=None

        else:
            prev2.next=self.head
            prev2=prev2.next
            self.head=self.head.next
            prev2.next=None

    prev1.next=d2.next
    self.head=d1.next
    return True

# for reversing just a few nodes inside the link list
def reverse_between(self,i1,i2):
    if self.head is None:
        return None
    
    current=self.head
    d=Node(0)
    d.next=current
    prev=d

    for _ in range(i1):
        current=current.next
        prev=prev.next

    to_move=current.next


    for _ in range(i2 - i1):
        current.next=to_move.next
        to_move.next=prev.next
        prev.next=to_move
        to_move=current.next

    self.head=d.next
    d.next=None

    return True

#there are better ways but this is what i thought of 
#there could be better ways and this is not one of the best
#its just the logic i used
def swap_pairs(self):
    if self.head is None:
        return False
    d=Node(0)
    first=self.head
    second=self.head.next
    d.next=self.head
    prev=d
        
    while second is not None:
        first.next=second.next
        second.next=prev.next
        prev.next=second
            
        if first.next is not None:
            prev=first
            first=first.next
            second=first.next
        else:
            second=None
            
            
            
    self.head=d.next
        
    return True