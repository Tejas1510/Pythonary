""""""""""""""""""""""""""""""""""""""
Name of Question:Palindrome Substring
Link of Question:https://www.codechef.com/problems/STRPALIN
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s1=input()
    a=list(s1)
    s2=input()
    b=list(s2)
    c=0
    for i in range(len(a)):
        if(a[i] in b):
            c=1
            break
    if(c==0):
        print("No")
    else:
        print("Yes")
