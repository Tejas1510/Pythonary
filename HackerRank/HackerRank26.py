""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Find Digit
Link of Question:https:https://www.hackerrank.com/challenges/find-digits/problem?h_r=next-challenge&h_v=zen
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count=0
    a=list(map(int,str(n)))
    for i in range(0,len(a)):
        a[i]=int(a[i])

        if(a[i]==0):
            c=2
        else:
            if(n%a[i]==0):
                count=count+1

    return count



if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        print(result)
