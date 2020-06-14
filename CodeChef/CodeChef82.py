""""""""""""""""""""""""""""""""""""""
Name of Question:Uniform String
Link of Question:https://www.codechef.com/problems/STRLBP
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    s=input()
    count=0
    for i in range(len(s)-1):
        if(s[i]!=s[i+1]):
            count=count+1
        else:
            pass
    if(count<=2):
        print('uniform')
    else:
        print("non-uniform")
