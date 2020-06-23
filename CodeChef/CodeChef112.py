""""""""""""""""""""""""""""""""""""""
Name of Question:Medel
Link of Question:https://www.codechef.com/problems/MDL
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    max1=max(a)
    min1=min(a)
    b=[]
    for i in range(len(a)):
        if(a[i]==max1 or a[i]==min1):
            b.append(a[i])
    print(*b)
