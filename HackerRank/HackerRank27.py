""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:sherlock and Square
Link of Question:https:https://www.hackerrank.com/challenges/sherlock-and-squares/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import math
import os
import random
import re
import sys

from math import ceil, sqrt
# Complete the squares function below.
def squares(l, r):
    count=0
     # Getting the very first number
    number = ceil(sqrt(l));

    # First number's square
    n2 = number * number;

    # Next number is at the difference of
    number = (number * 2) + 1;

    # While the perfect squares
    # are from the range
    while ((n2 >= l and n2 <= r)) :

        count=count+1

        # Get the next perfect square
        n2 = n2 + number;

        # Next odd number to be added
        number += 2;
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
