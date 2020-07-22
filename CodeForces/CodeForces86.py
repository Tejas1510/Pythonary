def before(x):
    if(x<5):
        if(x==4):
            return(2)
        elif(x==2):
            return(1)
        elif(x==3):
            return(2)
        elif(x==1):
            return(1)
        elif(x==0):
            return(0)
    elif(x==5):
        return(1)
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    x=abs(a-b)
    if(x<=5):
        ans=before(x)
        print(ans)
    else:
        ans=x%5
        ans1=x//5
        ans2=before(ans)
        print(ans1+ans2)
