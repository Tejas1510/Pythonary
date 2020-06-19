""""""""""""""""""""""""""""""""""""""
Name of Question:Change It
Link of Question:https://www.codechef.com/problems/CHNGIT
"""""""""""""""""""""""""""""""""""""""
from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    c=[]
    a=list(map(int,input().split()))
    b=Counter(a)
    for k,v in b.items():
        c.append(v)
    max1=max(c)
    c.remove(max1)
    print(sum(c))
