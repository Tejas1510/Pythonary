""""""""""""""""""""""""""""""""""""""
Name of Question:Drawing Book
Link of Question:https:https://www.hackerrank.com/challenges/drawing-book/problem?h_r=profile
"""""""""""""""""""""""""""""""""""""""

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
   a=(p-0)//2
   b=(n-p)//2
   c=min(a,b)
   return c

if __name__ == '__main__':


    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)
