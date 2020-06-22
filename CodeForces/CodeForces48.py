""""""""""""""""""""""""""""""""""""""
Name of Question:The New Year: Meeting Friends
Link of Question:https://codeforces.com/problemset/problem/723/A
"""""""""""""""""""""""""""""""""""""""
x1,x2,x3=map(int,input().split())
a1=[x1,x2,x3]
a=[x1,x2,x3]
max1=max(a)
min1=min(a)
a.remove(max1)
a.remove(min1)
for i in range(len(a)):
    middle=a[i]
for i in range(len(a1)):
    a1[i]=abs(a1[i]-middle)
print(sum(a1))
