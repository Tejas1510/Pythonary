#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    count1=0
    count2=0
    for i in range(0,len(a)):
        if(a[i]>b[i]):
            count1=count1+1
        elif(a[i]<b[i]):
            count2=count2+1

    result=[count1,count2]
    return result

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
