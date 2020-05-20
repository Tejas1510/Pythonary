""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Library Fine
Link of Question:https:https://www.hackerrank.com/challenges/library-fine/problem?h_r=next-challenge&h_v=zen
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if(y2>y1):
        return 0
    elif(y2==y1 and m2>m1):
        return 0
    elif(y2==y1 and m2==m1 and d2>d1):
        return 0
    elif(y2==y1 and m2==m1 and d2==d1):
        return 0
    elif(y2<y1):
        return 10000
    elif(y2==y1 and m2<m1):
        return 500*abs((m2-m1))
    elif(y2==y1 and m2==m1 and d2<d1):
        return 15*abs((d2-d1))




if __name__ == '__main__':


    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    print(result)
