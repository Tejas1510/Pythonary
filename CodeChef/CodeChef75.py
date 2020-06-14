""""""""""""""""""""""""""""""""""""""
Name of Question:Easy Math
Link of Question:https://www.codechef.com/problems/RPD
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    d=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if(i==j):
                pass
            else:
                b.append(a[i]*a[j])
    for i in range(len(b)):
        c=[int(j) for j in str(b[i])]
        d.append(sum(c))
    print(max(list(set(d))))
