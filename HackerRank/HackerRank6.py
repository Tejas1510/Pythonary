
"""""""""""""""""""""""""""""""""""""
Name of the problem:Apple and Oranges
Link to the problem:https:"//www.hackerrank.com/challenges/apple-and-orange/problem"
"""""""""""""""""""""""""""""""""""""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    new1=[]
    new2=[]
    count1=0
    count2=0
    for i in range(0,len(apples)):
        c=apples[i]+a
        new1.append(c)
        print(c)
        if(c in range(s,t+1)):
            count1=count1+1
    print(count1)
    for i in range(0,len(oranges)):
        d=oranges[i]+b
        new2.append(d)
        print(d)
        if(d in range(s,t+1)):
            count2=count2+1
    print(count2)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
