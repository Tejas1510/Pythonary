""""""""""""""""""""""""""""""""""""""
Name of Question:Mutated Minions 
Link of Question:https://www.codechef.com/problems/CHN15A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(len(a)):
        a[i]=a[i]+k
        if(a[i]%7==0):
            count=count+1
    print(count)
