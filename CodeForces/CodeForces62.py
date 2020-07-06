""""""""""""""""""""""""""""""""""""""
Name of Question:Vanya and Cards
Link of Question:https://codeforces.com/problemset/problem/401/A
"""""""""""""""""""""""""""""""""""""""
n,x=map(int,input().split())
a=list(map(int,input().split()))
if(sum(a)==0):
    print(0)
elif(abs(sum(a))<=x):
    print(1)
elif(abs(sum(a))>x):
    if((abs(sum(a)))%x==0):
        print((abs(sum(a)))//x)
    else:
        print((abs(sum(a)))//x+1)
