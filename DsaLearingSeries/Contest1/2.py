from collections import Counter
t=int(input())
for i in range(t):
    s=input()
    l=len(s)
    if(l%2==0):
        a=list(s[:l//2])
        b=list(s[l//2:])
    else:
        a=list(s[:l//2])
        b=list(s[l//2+1:])
    a=sorted(a)
    a1=Counter(a)
    b=sorted(b)
    b1=Counter(b)
    if(a1==b1):
        print("YES")
    else:
        print("NO")
