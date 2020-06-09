""""""""""""""""""""""""""""""""""""""
Name of Question:Chef and Table Tennis
Link of Question:https://www.codechef.com/problems/TTENIS
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()
    if(s.count("1")>s.count("0") and s.count("1")-s.count("0")>=2):
        print("WIN")
    else:
        print("LOSE")
