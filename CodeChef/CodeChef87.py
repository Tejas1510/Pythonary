""""""""""""""""""""""""""""""""""""""
Name of Question:Playing with String
Link of Question:https://www.codechef.com/problems/PLAYSTR
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    r=input()
    if(s.count("1")==r.count("1") and s.count("0")==r.count("0")):
        print("YES")
    else:
        print("NO")
