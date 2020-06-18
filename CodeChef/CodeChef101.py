""""""""""""""""""""""""""""""""""""""
Name of Question:Devu and Array
Link of Question:https://www.codechef.com/problems/DEVARRAY
"""""""""""""""""""""""""""""""""""""""
n,q=map(int,input().split())
a=list(map(int,input().split()))
a1=[]
a2=[]
for i in range(q):
    n1=int(input())
    a1.append(n1)
min1=min(a)
max1=max(a)
for i in range(len(a1)):
    if(min1<=a1[i]<=max1):
        print("Yes")
    else:
        print("No")
