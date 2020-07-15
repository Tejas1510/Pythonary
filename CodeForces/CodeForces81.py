t=int(input())
a=[]
b=[]
for i in range(t):
    l,r=map(int,input().split())
    a.append(l)
    b.append(r)
a1=a.count(0)
a2=a.count(1)
b1=b.count(0)
b2=b.count(1)
a3=min(a1,a2)
b3=min(b1,b2)
print(a3+b3)   
