""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and FRUITS
Link of Question:https://www.codechef.com/problems/FRUITS
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,m,k=map(int,input().split())
    if(abs(n-m)==k):
        print(0)
    elif(abs(n-m)>k):
        print(abs(n-m)-k)
    else:
        print(0)
