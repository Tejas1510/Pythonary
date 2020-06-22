""""""""""""""""""""""""""""""""""""""
Name of Question:Buy a Shovel
Link of Question:https://codeforces.com/problemset/problem/732/A
"""""""""""""""""""""""""""""""""""""""
k,r=map(int,input().split())
for i in range(1,10):
    if((k*i)%10==0 or (k*i)%10==r):
        print(i)
        break
    else:
        pass
