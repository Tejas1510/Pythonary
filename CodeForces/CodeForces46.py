""""""""""""""""""""""""""""""""""""""
Name of Question:Holiday Of Equality
Link of Question:https://codeforces.com/problemset/problem/758/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
a=list(map(int,input().split()))
max1=max(a)
a.remove(max1)
for i in range(len(a)):
    a[i]=max1-a[i]
print(sum(a))
