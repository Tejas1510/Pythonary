""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Doll
Link of Question:https://www.codechef.com/problems/MISSP
"""""""""""""""""""""""""""""""""""""""
from collections import Counter
t=int(input())
for i in range(t):
    a=[]
    n=int(input())
    for i in range(n):
        n1=int(input())
        a.append(n1)
    a.sort()
    b=Counter(a)
    c=[]
    d=[]
    for k,v in b.items():
        if(v%2!=0):
            print(k)
