""""""""""""""""""""""""""""""""""""""
Name of Question:Balanced Array
Link of Question:https://codeforces.com/problemset/problem/1343/B
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    n1=n/2
    if(n1%2!=0):
        print("NO")
    else:
        b1=[]
        b2=[]
        print("YES")
        for i in range(2,n+1,2):
            b1.append(i)
        for i in range(len(b1)-1):
            b2.append(b1[i]-1)
        b2.append(b1[-1]+(n//2)-1)
        b1.extend(b2)
        print(*b1)
