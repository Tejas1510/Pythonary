""""""""""""""""""""""""""""""""""""""
Name of Question:Chang and Bitwise OR 
Link of Question:https://www.codechef.com/problems/CHNGOR
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(len(a)):
        ans=ans|a[i]
    print(ans)
