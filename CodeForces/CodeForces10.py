""""""""""""""""""""""""""""""""""""""
Name of Question:Word Capitalization
Link of Question:https://codeforces.com/problemset/problem/281/A
"""""""""""""""""""""""""""""""""""""""
s=input()
a=list(s)
for i in range(len(a)):
    a[0]=a[0].upper()
    break
s="".join(a)
print(s)
