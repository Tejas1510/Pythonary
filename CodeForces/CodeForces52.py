""""""""""""""""""""""""""""""""""""""
Name of Question:Phoenix and Balance
Link of Question:https://codeforces.com/problemset/problem/1348/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append(pow(2,i))

    n1=int((n/2)-1)

    a1=a[:n1]
    a1.append(a[-1])
    a2=a[n1:n-1]
    print(abs(sum(a1)-sum(a2)))
