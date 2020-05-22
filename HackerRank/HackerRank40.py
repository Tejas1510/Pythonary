
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Modified Kaprekar Numbers
Link of Question:https://www.hackerrank.com/challenges/kaprekar-numbers/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    a=[]
    flag=0
    for i in range(p,q+1):
        if(i==1):
            print(1,end=" ")
            continue
        if(i==2 or i==3):
            continue
        n1=i*i

        n1=list(map(str,str(n1)))

        len1=len(n1)
        n2=n1[:len1//2]

        s1=""
        n2= s1.join(n2)


        n3=n1[len1//2:]
        n3= s1.join(n3)

        n4=int(n2)+int(n3)


        if(n4==i):
            print(n4,end=" ")
            flag=1
    if(flag==0):
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
