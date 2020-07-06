a,b,c,d=map(int,input().split())
e=[a,b,c]
e.sort()

max1=max(0,d-abs((e[0]-e[1])))
max2=max(0,d-abs((e[1]-e[2])))
print(max1+max2)
