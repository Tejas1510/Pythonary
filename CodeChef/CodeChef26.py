""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and digit of Number
Link of Question:https://www.codechef.com/problems/LONGSEQ
"""""""""""""""""""""""""""""""""""""""
from collections import Counter
t=int(input())
for i in range(t):
    n=input()
    a = [int(x) for x in str(n)]

    if(len(set(a))==1 and len(a)!=1):
        print("No")
    elif(len(set(a))==1 and len(a)==1):
        print("Yes")
    else:
        b=Counter(a)
        c=[]
        for k,v in b.items():
            c.append(v)
        if(1 not in c):
            print("No")
        else:
            print("Yes")
