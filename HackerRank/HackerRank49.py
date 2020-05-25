""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Lisa WorkBook
Link of Question:https://www.hackerrank.com/challenges/lisa-workbook/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 1;
    count = 0;
    for i in range(0,len(arr)):
        for j in range(1,arr[i]+1):
            if(j==page):
                  count=count+1
            if(j%k==0):
                  page=page+1
        if(arr[i]%k!=0):
              page=page+1

    return count;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
