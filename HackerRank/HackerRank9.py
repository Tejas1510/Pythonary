"""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Breaking Record
Quetion LinK:https:https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    count1=0
    count2=0
    min1=scores[0]
    max1=scores[0]
    for i in range(1,len(scores)):

        if(scores[i]>max1):
            count1=count1+1
            max1=scores[i]
        elif(scores[i]<min1):
            count2=count2+1
            min1=scores[i]
        else:
            pass
    return(count1,count2)

if __name__ == '__main__':


    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')
