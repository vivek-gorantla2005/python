class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def createnode(self,data):
        return Node(data)
    
    def insertbst(self,root,data):
        if(root is None):
            return Node(data)
        if(data<root.data ):
            root.left = self.insertbst(root.left,data)
        if(data>root.data):
            root.right = self.insertbst(root.right,data) 
        return root
    
    def disp(self,root):
        if(root is not None):
            self.disp(root.left)
            print(root.data)
            self.disp(root.right)

tree = Tree()
root = None
root = tree.insertbst(root,10)
root = tree.insertbst(root,20)
root = tree.insertbst(root,5)
tree.disp(root)