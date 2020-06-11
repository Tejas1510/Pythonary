""""""""""""""""""""""""""""""""""""""
Name of Question:Vanya and Fences
Link of Question:https://codeforces.com/problemset/problem/677/A
"""""""""""""""""""""""""""""""""""""""
n,h=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    if(a[i]>h):
        count=count+2
    else:
        count=count+1
print(count)
