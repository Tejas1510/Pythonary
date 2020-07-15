n=int(input())

if(n==1):
    print("O")
else:
    a=[0]*(1000+1)
    a[0]=0
    a[1]=1
    for i in range(2,1001):
        a[i]=a[i-1]+a[i-2]
    for i in range(1,n+1):
        if(i in a):
            print("O",end="")
        else:
            print("o",end="")
