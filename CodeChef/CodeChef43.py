""""""""""""""""""""""""""""""""""""""
Name of Question:Download File
Link of Question:https://www.codechef.com/problems/DWNLD
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    sum=0
    for i in range(n):

        t,d=map(int,input().split())
        if(k>t):
            k=k-t
            t=0
        else:
            t=t-k
            k=0
        sum=sum+(t*d)
    print(sum)
