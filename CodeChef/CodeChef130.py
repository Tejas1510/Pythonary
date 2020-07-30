t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a==0 and b==0):
        print(0)
    elif(a==0 or b==0):
        print(max(a,b))
    elif(a==b):
        print(a+b)
    elif(a%b==0 or b%a==0):
        print(max(a,b))
    else:
        print(2)
