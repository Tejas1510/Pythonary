""""""""""""""""""""""""""""""""""""""
Name of Question:Wrong Subtraction
Link of Question:https://codeforces.com/problemset/problem/977/A
"""""""""""""""""""""""""""""""""""""""
n,k=map(int,input().split())
while(k!=0):
    if(n%10==0):
        n=n//10
    else:
        n=n-1
    k=k-1
print(n)
