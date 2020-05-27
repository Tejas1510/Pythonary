""""""""""""""""""""""""""""""""""""""
Name of Question:Greed Puppy
Link of Question:https://www.codechef.com/problems/GDOG
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a=[]
    n,k=map(int,input().split())
    for i in range(1,k+1):
        a.append(n%i)
    print(max(a))
