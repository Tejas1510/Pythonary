""""""""""""""""""""""""""""""""""""""
Name of Question:Football
Link of Question:https://www.codechef.com/problems/MSNSADM1
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    c=[]
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(len(a)):
        res=20*a[i]-10*b[i]
        c.append(res)
    max1=max(c)
    if(max1<0):
        print(0)
    else:
        print(max1)
