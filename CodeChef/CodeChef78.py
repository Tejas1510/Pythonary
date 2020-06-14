""""""""""""""""""""""""""""""""""""""
Name of Question:A Balanced Contest
Link of Question:https://www.codechef.com/problems/PERFCONT
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    cake=0
    hard=0
    for i in range(len(a)):
        if(a[i]>=p//2):
            cake=cake+1
        elif(a[i]<=p//10):
            hard=hard+1
    if(cake==1 and hard==2):
        print("yes")
    else:
        print("no")
