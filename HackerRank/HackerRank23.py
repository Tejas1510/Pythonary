""""""""""""""""""""""""""""""""""""""
Name of Question:Save The Prisoner
Link of Question:https:https://www.hackerrank.com/challenges/save-the-prisoner/problem
"""""""""""""""""""""""""""""""""""""""



for _ in range(input()):
    n, m, s = map(int, raw_input().split())
    m %= n
    res = (m + s - 1) % n
    if res == 0:
        res = n
    print(res)
