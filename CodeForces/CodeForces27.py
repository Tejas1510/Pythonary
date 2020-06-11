""""""""""""""""""""""""""""""""""""""
Name of Question:Hulk
Link of Question:https://codeforces.com/problemset/problem/705/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
for i in range(n):
    if(i%2==0):
        if(i==n-1):
            print("I hate it",end=" ")
        else:
            print("I hate that",end=" ")
    else:
        if(i==n-1):
            print("I love it",end=" ")
        else:
            print("I love that",end=" ")
