""""""""""""""""""""""""""""""""""""""
Name of Question:Mishka and Game
Link of Question:https://codeforces.com/problemset/problem/703/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
m1=0
c1=0
for i in range(t):
    m,c=map(int,input().split())
    if(m>c):
        m1=m1+1
    elif(c>m):
        c1=c1+1
    else:
        pass
if(m1>c1):
    print("Mishka")
elif(m1<c1):
    print("Chris")
else:
    print("Friendship is magic!^^")
