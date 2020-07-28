n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if(a[i] not in b):
        b.append(a[i])
    else:
        b.remove(a[i])
        b.append(a[i])
print(len(b))
print(*b)
