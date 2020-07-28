from collections import Counter
n=int(input())
s=input()
a=list(s)
b=[]
c=[]
d=[]
e=[]
dict={}
count=0
for i in range(len(a)-1):
    a1=s[i:i+2]
    b.append(a1)
c=Counter(b)
for k,v in c.items():
    d.append(k)
    e.append(v)
max1=max(e)
ind=e.index(max1)
print(d[ind])
