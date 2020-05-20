#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, a):
    b=[]
    c=[]
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if(i==j):
                pass
            else:
                if((a[i]+a[j])%k!=0):
                    for i in range(0,len(b)):
                        if(b[i]+a[i]%k!=0 and b[i]+a[j]%k!=0):
                            b.append(a[i])
                            b.append(a[j])
    print(b)



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    nonDivisibleSubset(k, s)
