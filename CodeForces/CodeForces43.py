""""""""""""""""""""""""""""""""""""""
Name of Question:I_love_%username%
Link of Question:https://codeforces.com/problemset/problem/155/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
a=list(map(int,input().split()))
max1=a[0]
min1=a[0]
cmax=0
cmin=0
for i in range(1,len(a)):
    if(a[i]>max1):
        cmax=cmax+1
        max1=a[i]
    else:
        if(a[i]<min1):
            cmin=cmin+1
            min1=a[i]
print(cmax+cmin)
