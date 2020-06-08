""""""""""""""""""""""""""""""""""""""
Name of Question:Buying new Tablet
Link of Question:https://www.codechef.com/problems/TABLET
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a=[]
    n,b=map(int,input().split())
    for i in range(n):
        w,h,p=map(int,input().split())
        if(p>b):
            pass
        else:
            mul1=w*h
            a.append(mul1)
    if(len(a)==0):
        print("no tablet")
    else:
        print(max(a))
