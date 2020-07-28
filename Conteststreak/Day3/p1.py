n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(set(a))
if(len(b)<k):
    print("NO")
else:
    i=0
    print("YES")
    while(k!=0):
        print(a.index(b[i])+1,end=" ")
        i=i+1
        k=k-1
