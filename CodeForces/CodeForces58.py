""""""""""""""""""""""""""""""""""""""
Name of Question:Gennady and a Card Game
Link of Question:https://codeforces.com/problemset/problem/1097/A
"""""""""""""""""""""""""""""""""""""""
s=input()
a=list(s)
a1=list(map(str,input().split()))
count=0
for i in range(len(a1)):
    t=a1[i]
    if(t[0] in a or t[1] in a):
        count=count+1
    else:
        pass
if(count>=1):
    print("YES")
else:
    print("NO")
