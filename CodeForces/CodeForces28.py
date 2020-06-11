""""""""""""""""""""""""""""""""""""""
Name of Question:Magnets
Link of Question:https://codeforces.com/problemset/problem/344/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
a=[]
b=[]
count=0
for i in range(n):
    s=input()
    a.append(s)
a.append(str(11))
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        continue
    else:
        count=count+1
print(count)
