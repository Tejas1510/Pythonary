""""""""""""""""""""""""""""""""""""""
Name of Question:A Good Set
Link of Question:https://www.codechef.com/problems/GOODSET
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for _ in range(t):
    n=int(input())
    l1=[]
    odd=1
    while n>0:
        l1.append(odd)
        odd+=2
        n-=1
    print(*l1)
