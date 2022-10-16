# stack...........................................

# stack=[]
# def push():
#     element=input('enter element')
#     stack.append(element)
#     print(stack)

# def pop():
#     if not stack:
#         print('stack is empty')
#     else:
#         e=stack.pop(0)
#         print(e)
#         print(stack)
# while True:
#     print('enter your choice 1 for push, 2 fro pop , 3 for quit')
#     choice=int(input())
#     if choice==1:
#         push()
#     elif choice==2:
#         pop()
#     elif choice==3:
#         break
#     else:
#         print('wrong choice')


# queue-----------------------------------------------------

# queue=[]
# def enqueue():
#     element=input('enter element')
#     queue.append(element)
#     print(queue)

# def dequeue():
#     if not queue:
#         print('stack is empty')
#     else:
#         e=queue.pop()
#         print(e)
#         print(queue)
# while True:
#     print('enter your choice 1 for push, 2 fro pop , 3 for quit')
#     choice=int(input())
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     elif choice==3:
#         break
#     else:
#         print('wrong choice')

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


ll1=Linkdlist()

ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_end(30)
ll1.add_end(39)
ll1.add_after(100,20)
ll1.add_before(200,10)
ll1.delete_begin()
ll1.delete_begin()
ll1.print_LL()
