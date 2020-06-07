""""""""""""""""""""""""""""""""""""""
Name of Question:Way to long words
Link of Question:http://codeforces.com/problemset/problem/71/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()
    if(len(s)>10):
        print(s[0]+str(len(s)-2)+s[-1])
    else:
        print(s)
