""""""""""""""""""""""""""""""""""""""
Name of Question:Judging Dlay
Link of Question:https://www.codechef.com/problems/JDELAY
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    count=0
    n=int(input())
    for i in range(n):
        s,j=map(int,input().split())
        if(j-s>5):
            count=count+1
        else:
            pass
    print(count)
