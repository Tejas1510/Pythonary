""""""""""""""""""""""""""""""""""""""
Name of Question:Movie Weekend
Link of Question:https://www.codechef.com/problems/MOVIEWKN
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    e=[]
    for i in range(len(a)):
        c.append(a[i]*b[i])

    d=max(c)
    for i in range(len(c)):
        if(c[i]==d):
            e.append(i+1)
    if(len(e)==1):
        print(max(e))
    else:
        max1=b.index(max(b))
        max1=max1+1
        print(max1)
