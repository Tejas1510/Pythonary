""""""""""""""""""""""""""""""""""""""
Name of Question:Kitchen TimeTable
Link of Question:https://www.codechef.com/problems/KTTABLE
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    count=0
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    c.append(a[0])
    for i in range(len(a)-1):
        dif=a[i+1]-a[i]
        c.append(dif)
    for i in range(len(c)):
        if(c[i]>=b[i]):
            count=count+1
    print(count)
