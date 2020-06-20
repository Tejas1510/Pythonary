""""""""""""""""""""""""""""""""""""""
Name of Question:Hit the Lottery
Link of Question:https://codeforces.com/problemset/problem/996/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
a=[1,5,10,20,100]
count=0
while(n!=0):
    if(n>=a[-1]):
        n=n-a[-1]
        count=count+1
    else:
        a.pop()
print(count)
