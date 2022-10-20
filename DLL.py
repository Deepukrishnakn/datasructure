#DLL-------------------------------------------------------



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

    # def add_end(self,data):
    #     new_node=Node(data)
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         n=self.head
    #         while n is not None:
    #             n=n.nref
    #         n.nref = new_node
    #         new_node.pref=n
    
    def add_after(self,data,x):
        if self.head is None:
            print('list is empty')
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print('x not in the list')
            new_node=Node(data)
            new_node.nref=n.nref
            new_node.pref=n
            if n.nref is not None:
                n.pref=new_node
            n.nref=new_node
        
    def add_before(self,data,x):
        if self.head is None:
            print('list is empty')
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print('x is not in the list')
            else:
                new_node=Node(data)
                new_node.nref=n
                new_node.pref=n.pref
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    n.pref=new_node

    def delete_begin(self):
        if self.head is None:
            print('list is empty')
            return
        if self.head.nref is None:
            self.head = None
            print('list is empty after delete')
        else:
            self.head=self.head.nref
            self.head.pref=None

    def delete_last(self):
        if self.head is None:
            print('list is empty')
        elif self.head.nref is None:
            self.head=None
        else:
            n=self.head
            while n.nref.nref is not None:
                n=n.nref
            n.nref=None
         
    def delete_by_value(self,x):
        if self.head is None:
            print('list is empty')
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head=None
            else:
                print('x is not in the list')
                return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data == x:
                n.pref.nref=None
            else:
                print('x is not in the list')


dll1=DLL()

# dll1.add_empty_ll(10)
dll1.add_begin(10)
dll1.add_after(40,10)
dll1.add_before(50,40)
dll1.add_before(60,50)
# dll1.add_end(50)
# dll1.delete_last()
# dll1.delete_by_value(10)
dll1.print_DLL()

