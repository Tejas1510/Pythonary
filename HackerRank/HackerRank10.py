""""""""""""""""""""""""""""""""""""""
Name of Question:Birthday Chocolate
Link of Question:https://www.hackerrank.com/challenges/the-birthday-bar/problem
"""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count=0
    for i in range(n-m+1):
        if(sum(s[i:i+m])==d):
            count=count+1
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
