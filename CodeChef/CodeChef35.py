""""""""""""""""""""""""""""""""""""""
Name of Question:ATM Machine
Link of Question:https://www.codechef.com/problems/ATM2
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    for i in range(len(a)):
        if(a[i]<=k):
            k=k-a[i]
            b.append(str(1))
        else:
            b.append(str(0))
    s = ''.join(b)
    print(s)
