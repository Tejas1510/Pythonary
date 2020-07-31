


n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    if(a[i]<=k):
        count=count+1
    else:
        break
if(count==n):
    print(count)
else:
    b=a[::-1]
    for i in range(len(b)):
        if(b[i]<=k):
            count=count+1
        else:
            break    
    print(count)
