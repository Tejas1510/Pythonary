""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Employment test
Link of Question:https://www.codechef.com/problems/CK87MEDI
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    print(a[((n+k)//2)])
