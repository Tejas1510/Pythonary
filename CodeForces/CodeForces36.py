""""""""""""""""""""""""""""""""""""""
Name of Question:Amusing Joke
Link of Question:https://codeforces.com/problemset/problem/141/A
"""""""""""""""""""""""""""""""""""""""
s1=input()
s2=input()
s=s1+s2
large=input()
a=list(large)
flag=0
for i in range(len(s)):
    if(s[i] in a):
        a.remove(s[i])
    else:
        flag=1
        break
if(flag==1 or len(a)!=0):
    print("NO")
else:
    print("YES")
