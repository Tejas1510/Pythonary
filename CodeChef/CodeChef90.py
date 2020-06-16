""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and his daily routine
Link of Question:https://www.codechef.com/problems/CHEFROUT
"""""""""""""""""""""""""""""""""""""""
for _ in range(int(input())):
    s=input()
    if ('EC' in s) or ('SC' in s) or ('SE' in s):
        print('no')
    else:
        print('yes')
