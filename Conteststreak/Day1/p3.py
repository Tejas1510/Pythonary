n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
count=0
if(k==0):
    if((a[0]-1)>0):
        print(a[0]-1)
    else:
        print(-1)
else:
    ans=a[k-1]
    for i in range(len(a)):
        if(a[i]<=ans):
            count=count+1
    if(count<1 or count!=k):
        print("-1")
    else:
        print(ans)
