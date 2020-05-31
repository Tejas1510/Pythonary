""""""""""""""""""""""""""""""""""""""
Name of Question:Coins And Triangle
Link of Question:https://www.codechef.com/problems/TRICOIN
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    i=1
    count=0
    c=0
    while(count<=n):
        count+=i
        i=i+1
        c=c+1
    print(c-1)
