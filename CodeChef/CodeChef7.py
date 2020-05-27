t=int(input())
for i in range(t):
    n=int(input())
    if(n<1500):
        hra=0.1*n
        da=0.9*n
        print(n+hra+da)
    elif(n>=1500):
        hra=500
        da=0.98*n
        print(n+hra+da)
