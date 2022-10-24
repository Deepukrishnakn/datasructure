
class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return

        if self.key == data:
            return

        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    #BST_Search----------------------------------------------
    def search(self,data):
        if self.key == data:
            print('key is found')
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print('key is not found')
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print('key is not found')

    #preorder----------------------------------------------------
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    #Inorder------------------------------------------------------
    def inorder(self):
        if self.lchild:
            self.lchild.preorder()
        print(self.key)
        if self.rchild:
            self.rchild.preorder()

    #postorrder---------------------------------------------------
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)
    
    #delete----------------------------------------------------------
    def delete(self,data):
        if self.key is None:
            print('Tree is empty')
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print('node is not present')
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print('node is not present')
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                return temp
            node = self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self
            


root = BST(10)
list1=[3,5,44,21,7,5,90]
for i in list1:
    root.insert(i)
root.delete(10)
root.postorder()


