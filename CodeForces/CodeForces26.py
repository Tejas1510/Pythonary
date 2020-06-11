""""""""""""""""""""""""""""""""""""""
Name of Question:In Search of an Easy Problem
Link of Question:https://codeforces.com/problemset/problem/1030/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
a=list(map(int,input().split()))
if(a.count(1)>=1):
    print("HARD")
else:
    print("EASY")
