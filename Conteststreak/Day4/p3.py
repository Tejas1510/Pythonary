from collections import Counter
n,k=map(int,input().split())
s=input()
a=list(s)
b=sorted(a)
b=list(dict.fromkeys(b))
dict={}
for i in range(len(b)):
    dict[b[i]]=a.count(b[i])
print(dict)
i=0
while(k!=0):
    while(dict[i]!=0):
        a.remove(dict[i])
    k=k-dict[i]
print(a)
