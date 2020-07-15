t=int(input())
for i in range(t):
    count=0
    a,b,c=map(int,input().split())
    while(b!=0 and c//2>0):
        count=count+3
        b=b-1
        c=c-2
    while(a!=0 and b//2>0):
        count=count+3
        a=a-1
        b=b-2
    print(count)
