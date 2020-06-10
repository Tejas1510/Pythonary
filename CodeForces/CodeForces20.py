""""""""""""""""""""""""""""""""""""""
Name of Question:Word
Link of Question:https://codeforces.com/problemset/problem/59/A
"""""""""""""""""""""""""""""""""""""""
s=input()
upperc=0
lowerc=0
for i in range(len(s)):
    if(s[i].isupper()):
        upperc=upperc+1
    else:
        lowerc=lowerc+1
if(upperc>lowerc):
    print(s.upper())
else:
    print(s.lower())
