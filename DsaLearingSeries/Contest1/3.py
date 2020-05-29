t = int(input())
b=[]
for _ in range(t):
    b.append(int(input()))
b.sort()
c=[]
for i in range(len(b)):
   c.append(b[i]*(len(b)-i))
print(max(c))
