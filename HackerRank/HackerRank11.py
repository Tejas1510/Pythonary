#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n):
        for j in range(n):
            if(((ar[i]+ar[j])%k==0) and i!=j):
                count=count+1
    return int(count/2)






if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
