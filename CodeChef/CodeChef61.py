""""""""""""""""""""""""""""""""""""""
Name of Question:Find the Maximum Value
Link of Question:https://www.codechef.com/problems/LOSTMAX
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    a1=len(a)
    a1=a1-1
    a.remove(a1)
    print(max(a))
