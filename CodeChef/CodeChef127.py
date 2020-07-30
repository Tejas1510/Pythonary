t=int(input())
for i in range(t):
    n=int(input())
    max1=-9999999999
    for i in range(n):
        num=int(input())
        max1=max(num,max1)
    print(max1)
