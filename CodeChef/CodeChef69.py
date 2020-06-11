""""""""""""""""""""""""""""""""""""""
Name of Question:one more weird game
Link of Question:https://www.codechef.com/submit/complete/34180913
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print(n*(m-1)+m*(n-1))
