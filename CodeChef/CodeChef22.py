""""""""""""""""""""""""""""""""""""""
Name of Question:Forgotten Language
Link of Question:https://www.codechef.com/problems/FRGTNLNG
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    x=input().split(" ")
    p=[]
    for j in range(k):
        t=input().split()
        for k in t:
            p.append(k)

    for i in range(len(x)):

        if(x[i] in p):
            print("YES",end=" ")
        else:
            print("NO",end=" ")
    print("")
