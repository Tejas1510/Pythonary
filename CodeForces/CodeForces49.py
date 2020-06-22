""""""""""""""""""""""""""""""""""""""
Name of Question:Police Recruits
Link of Question:https://codeforces.com/problemset/problem/427/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
a=list(map(int,input().split()))
ans=0
count=0
for i in range(len(a)):
    if(a[i]==-1 and count==0):
        ans=ans+1
    elif(a[i]==-1 and count!=0):
        count=count-1
    else:
        count=count+a[i]
print(ans)
