""""""""""""""""""""""""""""""""""""""
Name of Question:Vision Control System
Link of Question:https://www.codechef.com/problems/VCS
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    count=0
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(len(a)):
        if(a[i] in b):
            count=count+1
    ans1=count
    a.extend(b)
    c=list(set(a))
    ans2=n-len(c)
    print(ans1,ans2)
