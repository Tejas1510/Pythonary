""""""""""""""""""""""""""""""""""""""
Name of Question:Two Arrays And Swaps
Link of Question:https://codeforces.com/problemset/problem/1353/B
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    sum1=sum(a)
    while(k!=0):
        max1=max(b)
        min1=min(a)
        a.remove(min1)
        b.remove(max1)
        a.append(max1)
        sum1=max(sum1,sum(a))
        k=k-1
    print(sum1)
