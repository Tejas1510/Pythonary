""""""""""""""""""""""""""""""""""""""
Name of Question:Days in Month
Link of Question:https://www.codechef.com/problems/NW1
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    num,day=map(str,input().split())
    num1=int(num)%7
    res=[4,4,4,4,4,4,4]
    week=["mon", "tues", "wed", "thurs", "fri", "sat","sun"]
    if(num1==0):
        print(*res)
    else:
        a=week.index(day)

        count=int(num)-28

        while(count!=0):
            res[a%7]=(res[a%7]+1)
            a=a+1
            count=count-1
        print(*res)
