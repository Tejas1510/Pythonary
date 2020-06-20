n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(n):
    for j in range(len(a)):
        if(i==a[j]):
            continue
        else:
            b2=abs(a[j]-i)
            b.append(b2)
    print(b)
    b3=max(b)
    print(b3)
    c.append(b3)
print(c)
