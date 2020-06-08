""""""""""""""""""""""""""""""""""""""
Name of Question:Lazy Zem
Link of Question:https://www.codechef.com/problems/TALAZY
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    Time=0
    count=0
    n,b,m=map(int,input().split())
    while(n!=0):
        if(n%2==0):
            n1=n//2
            Time=Time+n1*m+count

            n=n-n1
        else:
            n1=(n+1)//2
            Time=Time+n1*m+count

            n=n-n1
        count=b
        m=m*2

    print(Time)
