""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Glove
Link of Question:https://www.codechef.com/problems/CHEGLOVE
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    flag=0
    flag2=0
    flag4=0
    for i in range(len(a)):
        if(a[i]<=b[i]):
            pass
        else:
            flag2=2
            break
    b=b[::-1]
    for i in range(len(a)):
        if(a[i]<=b[i]):
            pass
        else:
            flag4=4
            break
    if(flag2==2 and flag4==4):
        print("none")
    elif(flag2==0 and flag4==0):
        print("both")
    elif(flag2==2 and flag4==0):
        print("back")
    elif(flag2==0 and flag4==4):
        print("front")
