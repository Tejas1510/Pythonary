""""""""""""""""""""""""""""""""""""""
Name of Question:Champak and Clocks
Link of Question:https://www.codechef.com/CROS2020/problems/COCR105
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    count=0
    for i in range(l,r):
        if(i==2 or i==8 or i==14 or i==20 ):
            count=count+1
        else:
            count=count+2
    if(r==9 or r==3 or r==21 or r==15):
        print(count+1)
    else:
        print(count)
