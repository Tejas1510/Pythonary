""""""""""""""""""""""""""""""""""""""
Name of Question:Divisibility Problem
Link of Question:https://codeforces.com/problemset/problem/1328/A
"""""""""""""""""""""""""""""""""""""""
from math import floor,ceil
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    count=0
    if(a%b==0):
        print(0)
    elif(a<b):
        print(b-a)
    else:
        c=ceil(a/b)
        print((b*c)-a)
