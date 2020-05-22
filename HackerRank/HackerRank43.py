""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Halloween Sale
Link of Question:https:https:https://www.hackerrank.com/challenges/halloween-sale/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    a=[]
    while(p>=m):
        a.append(p)
        p=p-d

    a1=sum(a)
    a2=s-a1
    if(s>a1):
        a1=sum(a)

        a2=s-a1

        print(len(a)+(a2//m))
    else:
        a1=sum(a)

        a2=a1-s

        a=a[::-1]

        count=0
        while(s>=a[-1]):
            s=s-a[-1]
            count=count+1
            a.pop()
        print(count)



if __name__ == '__main__':


    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    howManyGames(p, d, m, s)
