""""""""""""""""""""""""""""""""""""""
Name of Question:Football Match
Link of Question:https://www.codechef.com/problems/FBMT
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a=[]
    count=0
    n=int(input())
    for i in range(n):
        s=input()
        if(s not in a):
            a.append(s)
        if(a[0]==s):
            count=count+1
        else:
            count=count-1
    if(count>0):
        print(a[0])
    elif(count==0):
        print("Draw")
    else:
        print(a[1])
