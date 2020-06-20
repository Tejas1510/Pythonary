""""""""""""""""""""""""""""""""""""""
Name of Question:I Wanna Be the Guy
Link of Question:https://codeforces.com/problemset/problem/469/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
p=list(map(int,input().split()))
p.remove(p[0])
q=list(map(int,input().split()))
q.remove(q[0])
p.extend(q)
if(len(set(p))==n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
