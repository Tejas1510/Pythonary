""""""""""""""""""""""""""""""""""""""
Name of Question:Choosing Team
Link of Question:https://codeforces.com/problemset/problem/432/A
"""""""""""""""""""""""""""""""""""""""
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if(5-a[i]>=k):
        b.append(a[i])
print(len(b)//3)
