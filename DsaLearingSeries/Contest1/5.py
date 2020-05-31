""""""""""""""""""""""""""""""""""""""
Name of Question:Factorial
Link of Question:https://www.codechef.com/LRNDSA01/problems/FCTRL
"""""""""""""""""""""""""""""""""""""""
import math
t=int(input())
for i in range(t):
    count=0
    n=int(input())
    i=1
    while(n//math.pow(5,i)!=0):

        count=count+n//math.pow(5,i)
        i=i+1
    print(int(count))
