t=int(input())
sum1=0
sum2=0
sum3=0
for i in range(t):
    x,y,z=map(int,input().split())
    sum1=sum1+x
    sum2=sum2+y
    sum3=sum3+z
if(sum1==0 and sum2==0 and sum3==0):
    print("YES")
else:
    print("NO")
