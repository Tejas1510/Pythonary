""""""""""""""""""""""""""""""""""""""
Name of Question:Helpful Maths
Link of Question:https://codeforces.com/problemset/problem/339/A
"""""""""""""""""""""""""""""""""""""""
s=input()
s=s.replace("+","")
a=list(s)
a.sort()
for i in range(len(s)):
    if(i!=len(a)-1):
        print(str(a[i])+"+",end="")
    else:
        print(str(a[i]),end="")
