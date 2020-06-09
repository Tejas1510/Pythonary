""""""""""""""""""""""""""""""""""""""
Name of Question:Beautiful Matrix
Link of Question:https://codeforces.com/problemset/problem/263/A
"""""""""""""""""""""""""""""""""""""""
for i in range(1,6):
    a=input().split(" ")
    try:
        y=a.index("1")
        x=i
    except:
        pass
print(abs(x-3)+abs(y-2))
