""""""""""""""""""""""""""""""""""""""
Name of Question:Beautiful Year
Link of Question:https://codeforces.com/problemset/problem/271/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
while(True):
    n=n+1
    if(len(set(str(n)))==4):
        print(int(n))
        break
