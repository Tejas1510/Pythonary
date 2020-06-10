""""""""""""""""""""""""""""""""""""""
Name of Question:CV
Link of Question:https://www.codechef.com/problems/CV
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    if(len(s)==1):
        print(0)
    else:
        count=0
        a=["a","e","i","o","u"]
        for i in range(len(s)-1):
            if(s[i] not in a and s[i+1] in a):
                count=count+1
            else:
                pass
        print(count)
