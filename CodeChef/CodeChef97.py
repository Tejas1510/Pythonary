t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    a=list(s)
    for i in range(0,len(a)-1,2):
        a[i],a[i+1]=a[i+1],a[i]
    s="".join(a)
    print(s)
