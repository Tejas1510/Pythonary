""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Jumping on the Clouds: Revisited
Link of Question:https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    i=0
    n=len(c)
    while((i+k)%n!=0):
        i=(i+k)%n

        if(c[i]==1):
            e=e-1-2
        else:
            e=e-1
    return e


if __name__ == '__main__':


    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    if(c[0]==0):
        result=result-1
    elif(c[0]==1):
        result=result-3
    print(result)
