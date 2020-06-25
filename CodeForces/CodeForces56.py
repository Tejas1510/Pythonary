""""""""""""""""""""""""""""""""""""""
Name of Question:Short Substrings
Link of Question:https://codeforces.com/problemset/problem/1367/A
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()
    a1=[]
    for i in range(0,len(s),2):
        a=s[i:i+2]
        a1.append(a)
    s1=""
    for i in range(len(a1)-1):
        s1=s1+a1[i][0]
    s1=s1+a1[-1]
    print(s1)
