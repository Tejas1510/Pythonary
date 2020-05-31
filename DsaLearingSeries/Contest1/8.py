
def solve(k,d0,d1):
    i=2
    a=[d0,d1]
    while(i!=k):
        count=sum(a)%10
        a.append(count)
        i=i+1
    if(sum(a)%3==0):
        print("YES")
    else:
        print("NO")    
t=int(input())
for i in range(t):
    k,d0,d1=map(int,input().split())
    solve(k,d0,d1)
