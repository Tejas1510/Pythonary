n,m=map(int,input().split())
min1=999999999
for i in range(n):
    a,b=map(int,input().split())
    ans=(m/b)*a
    
    min1=min(ans,min1)
print(min1)
