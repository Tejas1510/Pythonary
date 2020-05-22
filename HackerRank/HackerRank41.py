""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Beautiful Triplets
Link of Question:https:https://www.hackerrank.com/challenges/beautiful-triplets/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, c):
    count=0
    for i in range(len(c)):
        if(c[i]+d in c and c[i]+2*d in c):
            count+=1
    print(count)
if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    beautifulTriplets(d, arr)
