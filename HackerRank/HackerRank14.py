""""""""""""""""""""""""""""""""""""""
Name of Question:Bon Appetite
Link of Question:https:https://www.hackerrank.com/challenges/bon-appetit/problem
"""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum=0
    for i in range(0,len(bill)):
        sum=sum+bill[i]
    sum=sum-bill[k]
    final=sum/2
    if(final<b):
        print(b-final)
    else:
        print("Bon Appetit")


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
