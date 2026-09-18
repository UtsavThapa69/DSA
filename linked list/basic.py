class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.length=1
        else:
            self.tail.next=new_node
            self.tail=new_node
        return True

    def pop(self):
        if self.head is None:
            return None
        elif self.length==1:
            temp=self.head
            self.head=None
            self.tail=None
            self.length=0
            return temp
        else:
            temp=self.head.next
            pre=self.head
            while temp.next:
                temp=temp.next
                pre=pre.next
            self.tail=pre
            pre.next=None
            self.length-=1
            return temp
    
    def prepend(self,value):       
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.length=1
        else:
            new_node.next=self.head
            self.head=new_node
        return True

    def pop_first(self):
        if self.head is None:
            return None
        elif self.length==1:
            temp=self.head
            self.head=None
            self.tail=None
            self.length=0
            return temp
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            self.length-=1
            return temp

    def get(self,index):
        temp=self.head
        if index<0 or index>=self.length:
            return None
        
        for _ in range(index):
            temp=temp.next
        return temp

    def set(self,index,value):
        temp=self.get(index)
        if temp is not None:
            temp.value=value
            return temp
        return None
    

    def insert(self,index,value):

        if index<0 or index>self.length:
            return False

        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        
        pre=self.get(index-1)
        curr=pre.next

        new_node=Node(value)
        pre.next=new_node
        new_node.next=curr
        self.length+=1
        return True

    def remove(self,index):

        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        pre=self.get(index-1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        return temp

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def reverse(self):
        if self.head is None:
            return None

        temp=self.head
        self.head=self.tail
        self.tail=temp
        before=None
        
#while temp is not None is more reliable though
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
        return True