""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Chocolate
Link of Question:https://www.codechef.com/problems/CHCHCL
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if(n%2!=0 and m%2!=0):
        print("No")
    else:
        print("Yes")
