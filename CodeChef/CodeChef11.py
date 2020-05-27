# """"""""""""""""""""""""""""""""""""""
# Name of Question:Three way communications
# Link of Question:https:https://www.codechef.com/problems/COMM3/
# """""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    count=0
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    if(((x2-x1)**2+(y2-y1)**2)**0.5<=n):
        count=count+1
    if(((x2-x3)**2+(y2-y3)**2)**0.5<=n):
        count=count+1
    if(((x3-x1)**2+(y3-y1)**2)**0.5<=n):
        count=count+1
    if(count>=2):
        print("yes")
    else:
        print("no")
