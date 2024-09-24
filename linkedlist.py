class Node:
    def __init__(self,data= None):
        self.data = data
        self.link = None
class LinkedList:
    def __init__(self):
        self.head = None
    def createnode(self,data):
        return Node(data) 
    def addnode(self,data):
        node = self.createnode(data)
        if(self.head is  None):
            self.head = node
        else:
            temp = self.head
            while(temp.link != None):

                temp = temp.link
            temp.link = node

    def addatbeg(self,data):
        node = self.createnode(data)
        if(self.head is None):
            return node
        else:
            node.link = self.head
            self.head = node


    def disp(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.link

list = LinkedList()
list.addnode(10)
list.addnode(20)
list.addnode(30)
list.addatbeg(40)
list.disp()