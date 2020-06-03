""""""""""""""""""""""""""""""""""""""
Name of Question:Alternating Subarray Prefix
Link of Question:https://www.codechef.com/problems/ALTARAY
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    w=[]
    for i in range(len(r)-2,-1,-1):
        if (r[i]>0 and r[i+1]<0) or (r[i]<0 and r[i+1]>0):
            count += 1
            w.append(count)
        else:
            count = 1
            w.append(count)
    w=w[::-1]
    w.append(1)
    for i in range(len(w)):
        print(w[i],end=" ")
