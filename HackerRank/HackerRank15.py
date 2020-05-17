""""""""""""""""""""""""""""""""""""""
Name of Question:Stock Market
Link of Question:https:https://www.hackerrank.com/challenges/sock-merchant/problem?h_r=next-challenge&h_v=zen
"""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    a=Counter(ar)
    b=[]
    c=[]

    for k,v in a.items():
        b.append(v)
    for i in range(0,len(b)):
        c.append(b[i]//2)
    d=sum(c)
    return d


if __name__ == '__main__':


    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
