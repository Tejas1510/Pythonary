""""""""""""""""""""""""""""""""""""""
Name of Question:Stones on the table
Link of Question:https://codeforces.com/problemset/problem/266/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
s=input()
a=list(s)
count=0
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        count=count+1
print(count)
