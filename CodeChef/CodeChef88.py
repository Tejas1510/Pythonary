""""""""""""""""""""""""""""""""""""""
Name of Question:Andrash and Stipendium 
Link of Question:https://www.codechef.com/problems/EGRANDR
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    avg=sum(a)/len(a)
    if(2 in a):
        print("No")
    elif(5 not in a):
        print("No")
    elif(avg<4):
        print("No")
    else:
        print("Yes")
