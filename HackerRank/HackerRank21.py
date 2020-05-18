""""""""""""""""""""""""""""""""""""""
Name of Question:Agry Professor
Link of Question:https:https://www.hackerrank.com/challenges/angry-professor/problem?h_r=next-challenge&h_v=zen
"""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    b=[]
    for i in range(0,len(a)):
        if(a[i]<=0):
            b.append(a)
    if(len(b)>=k):
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
