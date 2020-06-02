""""""""""""""""""""""""""""""""""""""
Name of Question:Farmer and his Plot
Link of Question:https://www.codechef.com/problems/RECTSQ
"""""""""""""""""""""""""""""""""""""""
from math import gcd
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=gcd(n,m)
    print(int(n/a)*int(m/a))
