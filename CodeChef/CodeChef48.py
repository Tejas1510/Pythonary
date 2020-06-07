""""""""""""""""""""""""""""""""""""""
Name of Question:STICKS
Link of Question:https://www.codechef.com/problems/STICKS
"""""""""""""""""""""""""""""""""""""""
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    list=[]
    l=[int(i) for i in input().split()]
    a=dict(Counter(l))
    for x,y in a.items():
        if y>1:
            list.append(x)
        if y>3:
            list.append(x)
    list.sort()

    if len(list)==1:
        print(-1)
    else:
        print((list[-1])*(list[-2]))
