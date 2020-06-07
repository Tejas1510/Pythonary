""""""""""""""""""""""""""""""""""""""
Name of Question:Count Subaray
Link of Question:https://www.codechef.com/problems/SUBINC
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    t=[0]*n
    for i in range(1,len(a)):
        if(a[i]>=a[i-1]):
            t[i]=t[i-1]+1

    print(sum(t)+n)
