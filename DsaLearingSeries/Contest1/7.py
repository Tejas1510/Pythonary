""""""""""""""""""""""""""""""""""""""
Name of Question:Laddu
Link of Question:https://www.codechef.com/LRNDSA01/problems/LADDU
"""""""""""""""""""""""""""""""""""""""

t=int(input())

for i in range(t):
    count=0
    n,origin=map(str,input().split())
    for i in range(int(n)):
        x=input()
        if("CONTEST_WON" in x):
             p=x.split()
             count=count+300
             if int(p[1])<20:
                count=count+20-int(p[1])
        if("TOP_CONTRIBUTOR" in x):
            count=count+300
        if("BUG_FOUND" in x):
            p=x.split()
            count=count+int(p[1])
        if("CONTEST_HOSTED" in x):
            count=count+50
    if(origin=="INDIAN"):
        print(int(count)//200)
    else:
        print(int(count)//400)
