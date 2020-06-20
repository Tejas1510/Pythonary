""""""""""""""""""""""""""""""""""""""
Name of Question:Ultra fast Mathematician
Link of Question:https://codeforces.com/problemset/problem/61/A
"""""""""""""""""""""""""""""""""""""""
s1=input()
s2=input()
a=list(s1)
b=list(s2)
c=[]
for i in range(len(a)):
    c.append(str(int(a[i])^int(b[i])))
s="".join(c)
print(s)
