t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    if(sum(a)>=m):
        print(m)
    elif(sum(a)<m):
        print(sum(a))
