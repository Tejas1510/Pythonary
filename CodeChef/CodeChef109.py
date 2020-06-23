""""""""""""""""""""""""""""""""""""""
Name of Question:Lift Request
Link of Question:https://www.codechef.com/problems/LIFTME
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    total=0
    curr=0
    for i in range(q):
        f,d=map(int,input().split())
        total=total+abs(curr-f)+abs(d-f)
        curr=d
    print(total)
