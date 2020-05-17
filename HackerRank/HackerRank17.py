""""""""""""""""""""""""""""""""""""""
Name of Question:Electronic Shop
Link of Question:https://www.hackerrank.com/challenges/electronics-shop/problem
"""""""""""""""""""""""""""""""""""""""


import sys


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = [int(keyboards_temp) for keyboards_temp in input().strip().split(' ')]
pendrives = [int(pendrives_temp) for pendrives_temp in input().strip().split(' ')]

max_spent = -1
for i in range(n):
    for j in range(m):
        total = keyboards[i] + pendrives[j]
        if total <= s and total > max_spent:
            max_spent = total

print(max_spent)
