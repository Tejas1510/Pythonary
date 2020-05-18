""""""""""""""""""""""""""""""""""""""
Name of Question:Picking Number
Link of Question:https://www.hackerrank.com/challenges/picking-numbers/problem
"""""""""""""""""""""""""""""""""""""""


import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

from collections import Counter
d = Counter(a)
ans = 0
for i in range(99):
    ans= max(d[i] + d[i+1], ans)
print(ans)
