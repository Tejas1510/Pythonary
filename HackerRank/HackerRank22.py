""""""""""""""""""""""""""""""""""""""
Name of Question:Viral Advertising
Link of Question:https://www.hackerrank.com/challenges/strange-advertising/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""""""""""""""""""""""""""""""""""""""


import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    a=2
    b=2
    for i in range(n-1):
        a=(a*3)//2
        b=b+a
    return b

if __name__ == '__main__':

    n = int(input())

    result = viralAdvertising(n)

    print(result)
