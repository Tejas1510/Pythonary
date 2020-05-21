""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Organizing Containers of Balls
Link of Question:https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import math
import os
import random
import re
import sys
import numpy as np
# Complete the organizingContainers function below.
def organizingContainers(container):
    for i in range(0,len(container)):
        a.append(sum(container[i][i:]))
    print(a)
    a=np.sum(container,axis=0)
    b=np.sum(container,axis=1)
    a=sorted(a)
    b=sorted(b)
    if(a==b):
        print("Possible")
    else:
        print("Impossible")



if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        organizingContainers(container)
