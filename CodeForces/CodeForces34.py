""""""""""""""""""""""""""""""""""""""
Name of Question:Pangram
Link of Question:https://codeforces.com/problemset/problem/520/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
s=input()
s=s.lower()
if(len(set(s))==26):
    print("YES")
else:
    print("NO")
