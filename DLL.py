#DLL-------------------------------------------------------

from hashlib import new


class Node():
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class DLL:
    def __init__(self):
        self.head = None

    def print_DLL(self):
        if self.head is None:
            print('list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data,end=' ')
                n=n.nref

    def print_DLL_reverce(self):
        if self.head is None:
            print('list is empty')
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end=' ')
                n=n.pref
                
    def add_empty_ll(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('list not empty')
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            new_node=self.head

    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            n=self.head
            while n is not None:
                n=n.nref
            n.nref = new_node
            new_node.pref=n


dll1=DLL()

# dll1.add_empty_ll(10)
# dll1.add_begin(20)

dll1.add_begin(20)
dll1.add_begin(30)
dll1.print_DLL()

