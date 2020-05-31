""""""""""""""""""""""""""""""""""""""
Name of Question:Factorial
Link of Question:https://www.codechef.com/LRNDSA01/problems/FCTRL
"""""""""""""""""""""""""""""""""""""""
def solve(i,n,q):
    if(n%2==0):
        print(n//2)
    elif(n%2!=0):
        if(i==q):
            print(n//2)
        else:
            print((n//2)+1)
t=int(input())
for i in range(t):
    g=int(input())
    for i in range(g):
        initial,n,q=map(int,input().split())
        solve(initial,n,q)
