""""""""""""""""""""""""""""""""""""""
Name of Question:Nearly Lucky Number
Link of Question:https://codeforces.com/problemset/problem/110/A
"""""""""""""""""""""""""""""""""""""""
n=input()
a=list(n)
if(a.count("4")+a.count("7")==4 or a.count("4")+a.count("7")==7):
    print("YES")
else:
    print("NO")
