t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            b.append(a[i]+a[j])
    
    max1=max(b)
    max1co=b.count(max1)
    print(max1co/len(b))
