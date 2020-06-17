""""""""""""""""""""""""""""""""""""""
Name of Question:Secret recipe
Link of Question:https://www.codechef.com/problems/CHEFRUN
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(len(a)-len(set(a)-set(b)))
