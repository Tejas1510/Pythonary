""""""""""""""""""""""""""""""""""""""
Name of Question:Strange operation
Link of Question:https://www.codechef.com/problems/UTMOPR
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if(k==1):
        if(sum(a)%2==0):
            print("odd")
        else:
            print("even")
    else:
        print("even")
