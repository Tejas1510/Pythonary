""""""""""""""""""""""""""""""""""""""
Name of Question:Root of Quadratic equation
Link of Question:https://www.codechef.com/problems/QUADROOT
"""""""""""""""""""""""""""""""""""""""
import math
a=int(input())
b=int(input())
c=int(input())
sqr=math.sqrt(b*b-4*a*c)
x1=(-b+sqr)/(2*a)
x2=(-b-sqr)/(2*a)
print(x1)
print(x2)
