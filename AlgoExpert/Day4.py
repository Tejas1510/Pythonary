# Find Closest value of a given Target value in binary search tree
# Here we will be given a target value and we need to find a node nearest to it in a given tree
#This question will give you insight about how to implement simple bibary search tree in python and finds the nearest value using Recursion

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
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
        else:
            self.data = data

    def solution(self,target,closest):
                currentNode=self.data
                if(abs(target-closest)>abs(target-self.data)):
                    closest=self.data
                if(target<self.data):
                    if self.left != None:
                        return self.left.solution(target,closest)
                    else:
                        return minVal
                elif(target>self.data):
                    if self.right != None:
                        return self.right.solution(target,closest)
                    else:
                        return closest
                else:
                    return minVal
    def findclosestvalueinbst(self,target):
                return self.solution(target,99999999)



t=int(input())
for i in range(t):
    n,target=map(int,input().split()) #no of nodes in tree
    a=list(map(int,input().split())) #nodes of tree in form of array
    root=Node(a[0])
    for i in range(1,len(a)):
        root.insert(a[i])
    ans=root.findclosestvalueinbst(target)
    print(ans)
