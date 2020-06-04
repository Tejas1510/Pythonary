""""""""""""""""""""""""""""""""""""""
Name of Question:Studying Alphabet
Link of Question:https://www.codechef.com/problems/ALPHABET
"""""""""""""""""""""""""""""""""""""""

s=input()
n=int(input())
for i in range(n):
    s1=input()
    a=list(s)
    b=list(s1)
    for i in range(len(b)):
        if(b[i] not in a):
            print("No")
            break
    else:
        print("Yes")
