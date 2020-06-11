""""""""""""""""""""""""""""""""""""""
Name of Question:IPL and RCB
Link of Question:https://www.codechef.com/problems/CLIPLX
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if(x<=y):
        print(0)
    else:
        print(x-y)
