""""""""""""""""""""""""""""""""""""""
Name of Question:Mathison and pangrams
Link of Question:https://www.codechef.com/problems/MATPAN
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    s=input()
    s=list(set(s))
    sum=0
    s1="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s1)):
        if(s1[i] in s):
            pass
        else:
            sum=sum+a[i]
    print(sum)
