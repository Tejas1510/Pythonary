""""""""""""""""""""""""""""""""""""""
Name of Question:Buggy Calculator
Link of Question:https://www.codechef.com/problems/BUGCAL
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    if(len(a)>len(b)):
        l=a
        s=b
    else:
        l=b
        s=a
    d=len(l)-len(s)
    result=l[:d]
    for i in range(len(s)):
        result=result+str((int(l[i+d])+int(s[i]))%10)
    print(int(result))
    result=""
