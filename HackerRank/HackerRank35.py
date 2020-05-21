""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Equalize the Array
Link of Question:https:https://www.hackerrank.com/challenges/equality-in-a-array/problem?h_r=next-challenge&h_v=zen
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the equalizeArray function below.
def equalizeArray(arr):
    a=[]
    arr=sorted(arr)
    c=Counter(arr)
    for k,v in c.items():
        a.append(v)
    max1=max(a)
    result=sum(a)-max1
    return result

if __name__ == '__main__':


    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)
