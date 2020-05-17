""""""""""""""""""""""""""""""""""""""
Name of Question:Cats and a Mouse
Link of Question:https:https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?h_r=next-challenge&h_v=zen
"""""""""""""""""""""""""""""""""""""""


import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if(abs(z-x)>abs(z-y)):
        print("Cat B")
    elif(abs(z-x)<abs(z-y)):
        print("Cat A")
    else:
        print("Mouse C")

if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        catAndMouse(x, y, z)
