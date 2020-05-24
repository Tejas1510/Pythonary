test=int(input())
for i in range (0,test):
    x=int(input())
    if((x/2)%1!=0):
        print(x*int((x/2)+1))
    else:
        print(int((x/2))*x)
