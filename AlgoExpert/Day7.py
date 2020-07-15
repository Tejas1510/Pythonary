# Find the node depth of a given binary search tree
# Here you have to find the depth of each and every node in the BST and add them up to get the final tatal depth
# It can be easily achieved with recursion
# Time Complexity:O(N) and Space Complexity:O(h) where h is height
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
    def solution(self,depth=0):
        if(self is None):
            return
        elif(self.left is None and self.right is None):
            return
        return depth+self.left.solution(depth+1)+self.right.solution(depth+1)
t=int(input())
for i in range(t):
    n=int(input()) # no of nodes in the tree
    a=list(map(int,input().split())) #value of each a[i] node
    root=Node(a[0])
    for i in range(1,len(a)):
        root.insert(a[i])
    ans=root.solution(0)
    print(ans)
