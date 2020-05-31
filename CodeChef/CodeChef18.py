""""""""""""""""""""""""""""""""""""""
Name of Question:Minimum and Maximum
Link of Question:https://www.codechef.com/problems/TWOSTR
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    i=0
    cost=0
    a.sort()
    while(len(a)!=1):
        b=[a[i],a[i+1]]
        c=max(b)
        d=min(b)
        a.remove(c)
        cost=cost+d
    print(cost)
