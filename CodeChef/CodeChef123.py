class Node:
    a=[]
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        print(self.data)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
    def PrintLeafNode(self):
        if(self.left==None and self.right==None):
            a.append(self.data)
        if(self.left):
            self.left.PrintLeafNode()
        if(self.right):
            self.right.PrintLeafNode()
        print(a)    

n=int(input())
a=list(map(int,input().split()))
root=Node(a[0])
for i in range(1,len(a)):
    root.insert(a[i])
root.PrintLeafNode()
