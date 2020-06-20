""""""""""""""""""""""""""""""""""""""
Name of Question:Restoring three Number
Link of Question:https://codeforces.com/problemset/problem/1154/A
"""""""""""""""""""""""""""""""""""""""
a,b,c,d=map(int,input().split())
arr=[a,b,c,d]
max1=max(arr)
arr.remove(max1)
for i in range(len(arr)):
    print(max1-arr[i],end=" ")
