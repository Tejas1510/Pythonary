""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and recipe
Link of Question:https://www.codechef.com/COOK118B/problems/CHEFRECP
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from collections import Counter
test = int(input())
for i in range(test):
    n=int(input())
    a = list(map(int,input().rstrip().split()))
    c=[]
    d=[]
    e=[]
    flag=0
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            continue
        else:
            if(a[i+1] not in e):
                e.append(a[i])
            else:
                flag=1
    b=Counter(a)
    for k,v in b.items():
        c.append(v)
    d=set(c)
    if(len(c)==len(d) and flag==0):
        print("YES")
    else:
        print("NO")
