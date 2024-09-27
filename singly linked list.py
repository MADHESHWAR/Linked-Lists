#create node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_list:
    def __init__(self):
        self.head=None
    #traversal
    def printLL(self):
        if self.head is  None:
            print("linked list is empty")
        else:
            n=self.head
            while(n is not None):
                print(n.data,end="-->")
                n=n.ref
    def add_begin(self,data):
        newnode=Node(data)
        newnode.ref=self.head
        self.head=newnode
    def add_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
    def after_add(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print("linked list is empty")
        else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode
    def before_add(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data==x:
            newnode=Node(data)
            newnode.ref=self.head

            self.head=newnode
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("linked list is empty")
        else:
            newnode=Node(data)
            newnode.ref=n.ref
            n.ref=newnode
    def insert_empty(self,data):
        if self.head is None:
            newnode=Node(data)
            self.head=newnode
        else:
            print("linkedlist is not empty ")
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("Linkedlist is empty")
        elif(self.head.ref is None):
            self.head=None
        else:
            n=self.head
            while(n.ref.ref is not None):
                n=n.ref
            n.ref=None
    def delete_by_value(self,x):
        if self.head is None:
            print("Linkedlist is empty")
            return
        if self.head.data ==x:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
                print("That element is not present in the linked list")
        else:
            n.ref=n.ref.ref
LL=Linked_list()
LL.add_begin(10)
LL.add_begin(20)
LL.add_begin(30)
LL.add_begin(40)    
LL.delete_by_value(10)
LL.printLL()
