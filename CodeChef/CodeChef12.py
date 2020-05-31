""""""""""""""""""""""""""""""""""""""
Name of Question:Closing the tweets
Link of Question:https://www.codechef.com/problems/TWTCLOSE
"""""""""""""""""""""""""""""""""""""""
n,k=map(int,input().split())
count=0
d=[]
for i in range(k):
    x=input()
    if("CLOSEALL" in x):
        count=0
        d=[]
    else:
        p=x.split()[1]
        if(p not in d):
            d.append(p)
            count=count+1
        else:
            d.remove(p)
            count=count-1

    print(count)
