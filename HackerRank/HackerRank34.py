""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Jumping on the Clouds
Link of Question:https:https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    n=len(c)
    i=0
    while(i!=n-1):
        if(c[(i+2)%n]!=1):
            i=i+2
            count=count+1
        else:
            i=i+1
            count=count+1

    return count

if __name__ == '__main__':


    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
