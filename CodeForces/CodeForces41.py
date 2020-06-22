""""""""""""""""""""""""""""""""""""""
Name of Question:Sum of Round Number
Link of Question:https://codeforces.com/problemset/problem/1352/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(i) for i in str(n)]
    b=[]
    count=0
    for i in range(len(a)):
        if(a[i]==0):
            pass
        else:
            b.append(str(a[i])+(len(str(n))-1-i)*"0")
            count=count+1
    print(count)
    for i in range(len(b)):
        print(int(b[i]),end=" ")
    print("")
