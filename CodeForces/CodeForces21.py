""""""""""""""""""""""""""""""""""""""
Name of Question:George and Accommodation
Link of Question:https://codeforces.com/problemset/problem/467/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
count=0
for i in range(t):
    p,q=map(int,input().split())
    if(q-p>=2):
        count=count+1
    else:
        pass
print(count)
