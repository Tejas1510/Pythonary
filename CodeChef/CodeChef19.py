""""""""""""""""""""""""""""""""""""""
Name of Question:Malvika is peculiar about color of balloons
Link of Question:https://www.codechef.com/problems/CHN09
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
    if(len(c)==1):
        print(0)
    else:
        print(min(c))
