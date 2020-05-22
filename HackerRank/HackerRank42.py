""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Minimum Distances
Link of Question:https://www.hackerrank.com/challenges/minimum-distances/problem?h_r=next-challenge&h_v=zen
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    d=[]
    for i in range(0,len(a)):
        if(a[i] in a):
            b=a.index(a[i])
            c=abs(b-i)
            d.append(c)
    d=list(set(d))
    if(len(d)==1):
        print("-1")
    else:
        d.remove(0)
        print(min(d))

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    minimumDistances(a)
