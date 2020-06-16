""""""""""""""""""""""""""""""""""""""
Name of Question:Secret recipe
Link of Question:https://www.codechef.com/problems/CHEFRUN
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    x1,x2,x3,v1,v2=map(int,input().split())
    d1=abs(x3-x1)
    d2=abs(x3-x2)
    if(d1/v1<d2/v2):
        print("Chef")
    elif(d1/v1>d2/v2):
        print("Kefa")
    else:
        print("Draw")
