
# Singly Linkidlist---------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkdlist:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print('LL is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        if n is None:
            print('x not inthe list')
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n is None:
            print('x is not in list')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    def delete_begin(self):
        if self.head is None:
            print('list is empty')
        else:
            self.head = self.head.ref


    def delete_last(self):
        if self.head is None:
            print('list is empty')
        elif self.head.ref is None:
            self.head = None
        else:
            n=self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref=None


ll1=Linkdlist()

ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_end(30)
ll1.add_end(39)
ll1.add_after(100,20)
ll1.add_before(200,10)
ll1.delete_last()
ll1.delete_last()
ll1.delete_begin()
ll1.print_LL()

