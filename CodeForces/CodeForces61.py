""""""""""""""""""""""""""""""""""""""
Name of Question:Vasya and Chocolate
Link of Question:https://codeforces.com/problemset/problem/1065/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s,a,b,c=map(int,input().split())
    print(s//c+((s//c)//a)*b)
