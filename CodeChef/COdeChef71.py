""""""""""""""""""""""""""""""""""""""
Name of Question:Temple Land
Link of Question:https://www.codechef.com/problems/TEMPLELA
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if(len(a)%2==0 or a[0]!=1 or a[-1]!=1):
        print("no")

    else:
        flag=0
        middle=len(a)//2
        for i in range(middle):
            if(a[i+1]!=a[i]+1):
                flag=1
                break
            else:
                continue
        for i in range(middle,len(a)-1,1):
            if(a[i+1]!=a[i]-1):
                flag=1
                break
            else:
                continue
        if(flag==1):
            print("no")
        else:
            print("yes")
