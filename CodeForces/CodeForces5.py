""""""""""""""""""""""""""""""""""""""
Name of Question:Dominos Piling
Link of Question:http://codeforces.com/problemset/problem/50/A
"""""""""""""""""""""""""""""""""""""""s
m,n=map(int,input().split())
if(m==1 and n==1):
    print(0)
else:
    print((m*n)//2)
