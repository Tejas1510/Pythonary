""""""""""""""""""""""""""""""""""""""
Name of Question:Anton and Polyhedrons
Link of Question:https://codeforces.com/problemset/problem/785/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
count=0
for i in range(t):
    s=input()
    if(s=="Tetrahedron"):
        count=count+4
    elif(s=="Cube"):
        count=count+6
    elif(s=="Octahedron"):
        count=count+8
    elif(s=="Dodecahedron"):
        count=count+12
    elif(s=="Icosahedron"):
        count=count+20
print(count)
