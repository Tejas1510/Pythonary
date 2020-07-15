t=int(input())
for i in range(t):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    while(d!=0):
        for i in range(1,len(a)):
            if(a[i]>0):
                a[i]=a[i]-1
                a[i-1]=a[i-1]+1
                break
        d=d-1
    print(a[0])
