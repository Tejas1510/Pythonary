""""""""""""""""""""""""""""""""""""""
Name of Question:Team Olympiad
Link of Question:https://codeforces.com/problemset/problem/490/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
a=list(map(int,input().split()))
dict=[]
if(len(set(a))!=3):
    print(0)
else:
    indA=[]
    indB=[]
    indC=[]
    a1=a.count(1)
    a2=a.count(2)
    a3=a.count(3)
    b=[a1,a2,a3]
    min1=min(b)
    print(min1)
    for i in range(len(a)):
        if(a[i]==1):
            indA.append(i)
        elif(a[i]==2):
            indB.append(i)
        else:
            indC.append(i)
    i=0
    while(min1!=0):
        print(indA[i]+1,end=" ")
        print(indB[i]+1,end=" ")
        print(indC[i]+1,end=" ")
        print("")
        i=i+1
        min1=min1-1
