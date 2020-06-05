""""""""""""""""""""""""""""""""""""""
Name of Question:Two Numbers
Link of Question:https://www.codechef.com/problems/TWONMS
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a,b,k=map(int,input().split())
    if(k%2==1):
        print(max(2*a,b)//min(2*a,b))
    else:
        print(max(a,b)//min(a,b))
