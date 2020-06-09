""""""""""""""""""""""""""""""""""""""
Name of Question:FlatLand
Link of Question:https://www.codechef.com/problems/ICL1902
"""""""""""""""""""""""""""""""""""""""
import math
from math import floor
t=int(input())
for i in range(t):
    count=0
    n=int(input())
    while(n!=0):
        n1=floor(math.sqrt(n))
        n2=n1*n1
        n=n-n2
        count=count+1
    print(count)
