""""""""""""""""""""""""""""""""""""""
Name of Question:Anton and Danik
Link of Question:https://codeforces.com/problemset/problem/734/A
"""""""""""""""""""""""""""""""""""""""
n=int(input())
s=input()
if(s.count("A")>s.count("D")):
    print("Anton")
elif(s.count("A")<s.count("D")):
    print("Danik")
else:
    print("Friendship")
