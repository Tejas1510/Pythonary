n=int(input())
a=[]
flag=0
for i in range(n):
    s=input()
    a.append(s)
a=sorted(a,key=len)

for i in range(len(a)-1):
    if(a[i+1].find(a[i])!=-1):
        pass
    else:

        flag=1
        break
if(flag==1):
    print("NO")
else:
    print("YES")
    for i in range(len(a)):
        print(a[i])
