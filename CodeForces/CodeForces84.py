n,m,z=map(int,input().split())
count=0
for i in range(1,z+1):
    if(i%n==0 and i%m==0):
        count=count+1
print(count)
