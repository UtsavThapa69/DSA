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
        
    