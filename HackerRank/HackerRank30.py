""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Cut the sticks
Link of Question:https:https://www.hackerrank.com/challenges/cut-the-sticks/problem
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from collections import Counter
def solve(arr):
    count=[]
    a=sorted(arr)
    c=Counter(a)
    for k,v in c.items():
        count.append(v)
    for i in range(len(count)):
        	print(sum(count[i:]))
n = int(input())

arr = list(map(int, input().rstrip().split()))

solve(arr)
