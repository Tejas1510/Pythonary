n=int(input())
a=list(map(int,input().split()))
if(len(a)%2!=0):
    a.sort()
    x=len(a)//2
    print(a[x])
else:
    a.sort()
    x=len(a)//2
    x=x-1
    print(a[x])