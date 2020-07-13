# Find the Sum of each branch of a given binay tree
# Suppose your tree has 5 branches then the sum array will consist of 5 elements
# If you properly debug the question using custom input you will realise the beauty of recurrsion
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
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
    def branchSum(self):
        sums=[]
        self.calculateBranchSum(0,sums)
        return sums
    def calculateBranchSum(self,runningSum,sums):
        newRunningSum=runningSum+self.data

        if(self.left is None and self.right is None):
            sums.append(newRunningSum)
            return sums


        self.left.calculateBranchSum(newRunningSum,sums)
        self.right.calculateBranchSum(newRunningSum,sums)

t=int(input())
for i in range(t):
    n=int(input()) # no of nodes in the tree
    a=list(map(int,input().split())) #value of each a[i] node
    root=Node(a[0])
    for i in range(1,len(a)):
        root.insert(a[i])
    ans=root.branchSum()
    print(ans)
