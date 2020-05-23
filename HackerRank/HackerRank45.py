""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:The Time in Words
Link of Question:https://www.hackerrank.com/challenges/the-time-in-words/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    nums = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen",
            "twenty", "twenty one", "twenty two",
            "twenty three", "twenty four",
            "twenty five", "twenty six", "twenty seven",
            "twenty eight", "twenty nine"];

    if (m == 0):
        print(nums[h], "o' clock");

    elif (m == 1):
        print("one minute past", nums[h]);

    elif (m == 59):
        print("one minute to", nums[(h % 12) + 1]);

    elif (m == 15):
        print("quarter past", nums[h]);

    elif (m == 30):
        print("half past", nums[h]);

    elif (m == 45):
        print("quarter to", (nums[(h % 12) + 1]));

    elif (m <= 30):
        print(nums[m],"minutes past", nums[h]);

    elif (m > 30):
        print(nums[60 - m], "minutes to",
              nums[(h % 12) + 1]);

if __name__ == '__main__':

    h = int(input())

    m = int(input())

    timeInWords(h, m)
