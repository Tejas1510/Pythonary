""""""""""""""""""""""""""""""""""""""
Name of Question:Average Number
Link of Question:https://www.codechef.com/problems/AVG
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k,v=map(int,input().split())
    a=list(map(int,input().split()))
    a1=v*(n+k)-sum(a)
    if((a1%k==0) and (a1//k>0)):
        print(a1//k)
    else:
        print(-1)
