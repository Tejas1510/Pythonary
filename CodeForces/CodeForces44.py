""""""""""""""""""""""""""""""""""""""
Name of Question:New Year and Hurry
Link of Question:https://codeforces.com/problemset/problem/750/A
"""""""""""""""""""""""""""""""""""""""
n,k=map(int,input().split())
time=240-k
i=1
count=0
while(time>=0):
    time=time-5*i

    i=i+1
    if(time>=0):
        count=count+1
    else:
        pass
if(count>n):
    print(n)
else:
    print(count)
