""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Eid
Link of Question:https://www.codechef.com/problems/EID
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a=sorted(a)
    min1=9999999
    for i in range(0,len(a)-1):
        min1=min(min1,abs(a[i]-a[i+1]))
    print(min1)
