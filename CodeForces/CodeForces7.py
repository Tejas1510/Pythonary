""""""""""""""""""""""""""""""""""""""
Name of Question:Petya and Strings
Link of Question:https://codeforces.com/problemset/problem/112/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
if(s1==s2):
    print(0)
elif(s1<s2):
    print(-1)
else:
    print(1)
