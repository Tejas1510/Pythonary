""""""""""""""""""""""""""""""""""""""
Name of Question:BackGold Problem
Link of Question:https://codeforces.com/problemset/problem/749/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
if(n%2==0):
    k=n//2
    print(k)
    for i in range(k):
        print(2,end=" ")
else:
    k=n//2
    print(k)
    for i in range(k-1):
        print(2,end=" ")
    print(3,end=" ")
