""""""""""""""""""""""""""""""""""""""
Name of Question:Tickets
Link of Question:https://www.codechef.com/problems/TICKETS5
"""""""""""""""""""""""""""""""""""""""
t=int(input())
for i in range(t):
    flag=0
    s=input()
    if(s[0]==s[1]):
        flag=1

    for i in range(0,len(s)-2,2):
        if(s[i]!=s[i+2]):
            flag=1

    for i in range(1,len(s)-2,2):
        if(s[i]!=s[i+2]):
            flag=1

    if(flag==1):
        print("NO")
    else:
        print("YES")
