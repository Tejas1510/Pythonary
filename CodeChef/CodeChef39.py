""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Coloring
Link of Question:https://www.codechef.com/problems/COLOR
"""""""""""""""""""""""""""""""""""""""
from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    a=list(s)
    b=Counter(a)
    c=[]
    for k,v in b.items():
        c.append(v)
    d=max(c)
    sum1=sum(c)
    sum1=sum1-d
    print(sum1)
