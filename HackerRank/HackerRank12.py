#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys
import statistics
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    res = max(set(arr), key = arr.count)
    return(res)
if __name__ == '__main__':


    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
