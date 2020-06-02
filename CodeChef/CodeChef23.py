""""""""""""""""""""""""""""""""""""""
Name of Question:Piece of Cake
Link of Question:https://www.codechef.com/problems/LCH15JAB
"""""""""""""""""""""""""""""""""""""""
from collections import Counter
t=int(input())
for i in range(t):
    s=input()
    a=list(s)
    b=Counter(a)
    c=[]
    for k,v in b.items():
        c.append(v)
    d=max(c)
    c.remove(d)
    e=sum(c)
    if(d==e):
        print("YES")
    else:
        print("NO")
