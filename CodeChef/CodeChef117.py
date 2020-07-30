""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question:Fancy quotes
Link of Question:https://www.codechef.com/problems/FANCY
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input().split(" ")

    if("not" in s):
        print("Real Fancy")
    else:
        print("regularly fancy")
