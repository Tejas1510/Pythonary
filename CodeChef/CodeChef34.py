""""""""""""""""""""""""""""""""""""""
Name of Question:Chef And price control
Link of Question:https://www.codechef.com/JUNE20B/problems/PRICECON
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans1=sum(a)
    b=[]
    for i in range(len(a)):
        if(a[i]>k):
            a[i]=k
            b.append(a[i])
        else:
            b.append(a[i])
    ans2=sum(b)
    print(ans1-ans2
