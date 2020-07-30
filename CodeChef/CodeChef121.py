t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(len(a)):
        if(a[i]>=x):
            count=count+1
        else:
            pass
    if(count>=1):
        print("YES")
    else:
        print("NO")
