n=int(input())
a=[]
count=0
for i in range(n):
    l,r=map(int,input().split())
    a.append([l,r])
k=int(input())
for i in range(len(a)):
    if(k<=a[i][1]):
        count=count+1
print(count)
