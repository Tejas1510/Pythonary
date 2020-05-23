""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Chocolate Feast
Link of Question:https:https://www.hackerrank.com/challenges/chocolate-feast/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys


def chocolateFeast(n, c, m):
    n1=n/c
    if(n1<m):
        print(int(n1))
    elif(n1==m):
        print(int(n1+1))
    else:
        ch = n//c
        all_ch = ch
        while (m<=ch):
                all_ch += ch//m
                ch = ch//m + ch%m
        print(all_ch)

if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        chocolateFeast(n, c, m)
