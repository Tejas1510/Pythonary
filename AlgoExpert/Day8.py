# implementing Depth first Search for traversing a graph or a tree
# Time complexity is O(V+E) and Time complexity is O(V)
# where V is no of vertices and E is no of edges

class Node:
    def __init__(self,data):
        self.children=[] #it makes a empty children array
        self.data=data;  #assign the root value

    # This function add all the children node of the present root node to children array
    def addChild(self,data):
        self.children.append(Node(data))

    def DFS(self,array):
        array.append(self.data)
        for i in self.children:
            i.DFS(array)
        return array
        
